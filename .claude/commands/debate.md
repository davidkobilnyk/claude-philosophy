---
description: Stage a philosophical debate between the rationalist and naturalist agents
argument-hint: [motion] [--rounds N] [--save]
---

Stage a debate between `philosopher-rationalist` (Theo) and `philosopher-naturalist` (Nora) on: **$ARGUMENTS**

## Setting the motion

If no motion was given, propose four and ask the user to pick — a spread across mind, ethics, knowledge and metaphysics, phrased as propositions someone could actually deny. If the motion given is vague ("consciousness", "ethics"), sharpen it into a proposition and say which sharpening you chose before starting.

Assign sides by which position each agent's commitments genuinely support. If the motion cuts against type — a motion the naturalist would naturally affirm — say so and let each argue the side they believe, rather than forcing the pairing.

Default `--rounds` is 3. `--save` writes the transcript to `debates/<slug>.md`.

## Running it

Each turn is one `Agent` call with `run_in_background: false` — the debate is strictly sequential, since each reply answers the last.

1. **Openings.** Spawn Theo with the motion and his side; then Nora with the motion, her side, and Theo's full opening text.
2. **Exchanges.** For each round, continue the *existing* agent with `SendMessage` (not a fresh `Agent` call — they need their own context to avoid repeating themselves) and pass the opponent's last reply verbatim. Alternate. Do not summarise, soften or improve either side's text in transit; relay it whole.
3. **Closings.** One final turn each, capped at 200 words: what they showed, what they conceded, what the disagreement now rests on.

Print every turn to the user as it arrives, under a heading naming the speaker and round. Never write a turn yourself, never fill in a gap if an agent returns something thin — send it back for another pass instead.

## Adjudication

After the closings, write **Where it stands** in your own voice, under 300 words:

- The single point of disagreement the debate actually reduced to, stated so both would recognise it.
- What each side conceded, quoted.
- Which arguments landed and which were dodged — name the dodge if there was one.
- The load-bearing premise that, if it flipped, would flip the debate.

Judge the arguments, not the debaters, and do not declare a winner unless one side's case actually collapsed. Saying the disagreement is real and bottoms out in a genuine difference of starting points is a legitimate verdict; forced balance is not — if one side was clearly stronger, say that plainly.
