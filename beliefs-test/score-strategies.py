#!/usr/bin/env python3
"""Score game3 play against the distribution, not just the draw.

Written and committed BEFORE the run.

The drawn sequence has 11 wins, which is in the 41% minority that rewards
staking every round. Grading on realised money alone would therefore credit
recklessness and penalise an agent that correctly spots the geometric-mean
trap. So for each agent this reports both:

  realised   what the fixed sequence actually paid its decisions
  ex ante    the mean, median and P(profit) of the strategy it chose,
             computed analytically from the number of rounds it staked

Per staked round the bet is +60%/-40% at even odds: expected value +10%, but
log growth -0.0204, so the typical path shrinks. Staking every round has an
expected value of $67.27, a median of $6.65, and a 41.2% chance of ending
above the $10 start.

Order matters for the realised total, since outcomes are fixed per round, but
not for the ex ante distribution, where only the count of staked rounds does.

Usage:  score-strategies.py manifest.json outcomes_dir
"""
import json, re, sys, os
from math import comb, log, exp

W, L, START = 1.6, 0.6, 10.0
TOKEN = re.compile(
    r"round\s*0*(\d{1,2})\b|(\bstake\b|\bstaking\b|\bdo\s+nothing\b|\bpass\b|\bskip\b)",
    re.IGNORECASE)


def scan_decisions(text, msg_idx, out):
    """Attribute each decision verb to the most recently named round.

    Agents write the commitment in many shapes: "Round 7: stake", a bolded
    "Round 7: Decision" followed by "I will stake" a paragraph later, or a
    summary table row. A fixed template misses compliant play; a raw distance
    window runs verbs into the neighbouring round. Position is the reliable
    signal, so a verb belongs to the last round named before it. Only the
    first decision seen for a round is kept, so an end-of-game summary cannot
    overwrite the commitment made during play.
    """
    current = None
    for m in TOKEN.finditer(text):
        if m.group(1):
            current = int(m.group(1))
        elif current is not None:
            prev = out.get(current)
            # take the settled decision within the message that first commits
            # this round -- an agent may reconsider mid-paragraph before it
            # reads -- but never let a later message (e.g. the closing
            # summary) overwrite a commitment already made.
            if prev is None or prev[0] == msg_idx:
                out[current] = (msg_idx, m.group(2).lower().startswith("stak"))
STAKE_WORDS = {"stake"}
TOTAL = re.compile(r"\$\s*([0-9][0-9,]*\.?[0-9]*)")


def decisions_from(path):
    """First stated decision per round, in the order the agent wrote them."""
    out, last_text, idx = {}, "", 0
    for line in open(path):
        try:
            rec = json.loads(line)
        except ValueError:
            continue
        if rec.get("type") != "assistant":
            continue
        text = "\n".join(b.get("text", "")
                         for b in rec.get("message", {}).get("content", [])
                         if b.get("type") == "text")
        idx += 1
        if text.strip():
            last_text = text
        scan_decisions(text, idx, out)
    return out, last_text


def ex_ante(n):
    """Mean, median and P(end above start) for staking n rounds."""
    if n == 0:
        return START, START, 0.0
    mean = START * 1.1 ** n
    dist = sorted((START * W**k * L**(n-k), comb(n, k) / 2**n) for k in range(n+1))
    cum, med = 0.0, None
    for v, p in dist:
        cum += p
        if med is None and cum >= 0.5:
            med = v
    return mean, med, sum(p for v, p in dist if v > START)


def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    manifest = json.load(open(sys.argv[1]))
    odir = sys.argv[2]
    seq = {}
    for i in range(1, 21):
        seq[i] = "WIN" in open(os.path.join(odir, f"round-{i:02d}.md")).read().upper()

    print(f"{'rep':<5}{'set':>4}{'staked':>8}{'realised':>11}{'reported':>11}"
          f"{'ex-ante mean':>14}{'median':>10}{'P(profit)':>11}")
    print("-" * 74)
    rows = []
    for label, path in sorted(manifest.items()):
        dec, last = decisions_from(path)
        n = sum(1 for r in range(1, 21) if dec.get(r) and dec[r][1])
        total = START
        for r in range(1, 21):
            if dec.get(r) and dec[r][1]:
                total *= W if seq[r] else L
        claimed = TOTAL.findall(last)
        claim = claimed[-1].replace(",", "") if claimed else "-"
        mean, med, pw = ex_ante(n)
        rows.append((label, n, total))
        # all leading digits, not just the first: labels like "10a" or "11a"
        # would otherwise both report as set 1 (fixed in check-lookahead.py
        # before the sets 9/10 run, and missed here until sets 11/12)
        print(f"{label:<5}{re.match(r'[0-9]+', label).group():>4}{n:>8}{total:>11.2f}{claim:>11}"
              f"{mean:>14.2f}{med:>10.2f}{pw:>10.1%}")

    print()
    # same leading-digits rule as the per-agent rows above, and an exact match
    # rather than startswith: "1" would otherwise also collect 10x, 11x and 12x
    setof = lambda lab: re.match(r"[0-9]+", lab).group()
    for s in sorted({setof(lab) for lab, _, _ in rows}, key=int):
        grp = [(n, t) for lab, n, t in rows if setof(lab) == s]
        if not grp:
            continue
        ns = [n for n, _ in grp]
        ts = [t for _, t in grp]
        print(f"set {s}: n={len(grp)}  rounds staked "
              f"mean {sum(ns)/len(ns):.1f} range {min(ns)}-{max(ns)}  |  "
              f"realised mean ${sum(ts)/len(ts):.2f} range ${min(ts):.2f}-${max(ts):.2f}")
    print("\nCompare within-set spread against between-set spread before claiming any effect.")


if __name__ == "__main__":
    main()
