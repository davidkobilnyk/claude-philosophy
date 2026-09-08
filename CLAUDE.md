# claude-philosophy

## Pull requests

After making changes, check whether there is an open pull request for the current branch
before doing anything else with git.

- **If an open PR exists for this branch**, push to it. Do not open a second one.
- **If the branch's PR is already merged**, it is finished and cannot carry new work. Start
  the branch again from the latest `main` and open a new PR.
- **If there is no PR**, create one, as ready for review rather than a draft.

Do this proactively — do not wait to be asked, and do not leave work committed locally
where it cannot be reviewed. The point is that a human can see every change.

A merged PR means `main` has moved. Re-check before branching.

## What this repository is

Two lines of work:

- `.claude/agents/philosopher-*.md` and `.claude/commands/debate.md` — two agents with
  opposed philosophical commitments that debate a motion. Transcripts in `debates/`.
- `beliefs-test/` — an experiment asking whether giving an agent a belief set changes its
  behaviour on tasks unrelated to those beliefs. See `beliefs-test/README.md`.

## Conventions that protect the experiment

These exist because breaking them silently invalidates results rather than causing an
obvious failure.

**Agent file text is a treatment, not just configuration.** `beliefs-test`'s results were
produced under specific wording. Editing a `belief-player-*.md` file changes what the
agents receive, so any comparison against earlier numbers stops being valid. If a refactor
is worth doing, re-run the conditions being compared under the new version rather than
comparing across versions.

**Analysis scripts are committed before the run they analyse.** `check-lookahead.py` and
`score-strategies.py` are written and tested against fixtures first, so their criteria
cannot be adjusted to fit whatever the data turns out to look like. If a script has to
change after a run, it should be because it mis-parses compliant behaviour — verify the
claim against the raw transcripts, fix the parser, and record what changed and why.

**Randomness is fixed and disclosed.** Game outcome sequences are generated once from a
documented seed and shared by every agent, so results reflect decisions rather than luck.
Regenerating a sequence because the draw looks unhelpful is p-hacking; use what came out
and note its properties.

**Capture agent output from the harness, not from the agents.** Asking a player to write
its own transcript gives it a second task the rules never set, and produces composed
reports rather than a record. Extract the raw text from the harness JSONL afterwards.
