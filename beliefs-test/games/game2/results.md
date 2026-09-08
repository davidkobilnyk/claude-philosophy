# Game 2 results

Two ropes, inconsistent burn rates, measure 45 minutes. Accuracy first, speed second.
Haiku 4.5, 8 replicas (4 per belief set), launched together, 60-second clock.

## Outcome

All 8 answered correctly: light rope A at both ends and rope B at one end; when A is
consumed 30 minutes have passed, then light B's second end and its remaining 30 minutes
of rope burns in 15. Total 45.

No replica was stopped by the clock — all finished in 19-25 seconds.

Word counts and belief mentions below are measured on the raw generated text in
`output-*.md`, not on any file the agents authored.

| Replica | Set | Duration | Tokens | Tool calls | Words | Belief mentions |
|---|---|---|---|---|---|---|
| 1a | 1 | 21.0s | 9291 | 4 | 234 | 3 |
| 1b | 1 | 20.7s | 9238 | 3 | 273 | 2 |
| 1c | 1 | 23.0s | 9434 | 3 | 343 | 3 |
| 1d | 1 | 25.4s | 9640 | 3 | 431 | 6 |
| 2a | 2 | 18.7s | 9024 | 3 | 164 | 3 |
| 2b | 2 | 23.0s | 9599 | 4 | 311 | 2 |
| 2c | 2 | 22.0s | 9397 | 3 | 289 | 3 |
| 2d | 2 | 19.8s | 9262 | 4 | 343 | 2 |

## Reading

Accuracy is uninformative — the puzzle has one clean answer and every replica found it.

On the behavioural measures, within-set spread exceeds between-set spread on every dimension.
Word counts overlap almost completely (set 1: 234-431, set 2: 164-343), and belief mentions are
near-identical (3/2/3/6 against 3/2/3/2), with 1d the only outlier in either direction. Set 1's
own range on word count is wider than the gap between the set means. **No claim of a belief
effect is supportable from this run.**

Every replica read its belief file, none used it to solve the puzzle, and mentions of it were
confined to procedural notes about what had been read.

## Confound in the first two games

Both game1 and game2 ran with agent files that instructed each player to author and maintain a
transcript file. That was a second task nothing in the rules asked for, and it made the players
narrate themselves and compose reports. The authored files have been discarded in favour of the
raw generated text, which the harness records independently.

Recomputing on raw text changed the picture: the authored files suggested set 1 mentioned its
beliefs far more often than set 2 (0/1/5/3 against 0/1/1/0), which turned out to be an artifact
of document formatting rather than a difference in behaviour.

The transcript instruction has since been removed from both agent files, along with their Write
tool. Output for later games is captured from the harness after the fact, so players do nothing
but read their beliefs, read the rules, and play.

## Caveat on the token counts

These are near-identical (9024-9640) because most of each budget is fixed cost — system prompt,
belief file, rules file — not reasoning. They measure the harness, not the thinking.
