# Game 2 results

Two ropes, inconsistent burn rates, measure 45 minutes. Accuracy first, speed second.
Haiku 4.5, 8 replicas (4 per belief set), launched together, 60-second clock.

## Outcome

All 8 answered correctly: light rope A at both ends and rope B at one end; when A is
consumed 30 minutes have passed, then light B's second end and its remaining 30 minutes
of rope burns in 15. Total 45.

No replica was stopped by the clock — all finished in 19-25 seconds.

| Replica | Set | Duration | Tokens | Tool calls | Words | Belief/philosophy mentions |
|---|---|---|---|---|---|---|
| 1a | 1 | 21.0s | 9291 | 4 | 311 | 0 |
| 1b | 1 | 20.7s | 9238 | 3 | 290 | 1 |
| 1c | 1 | 23.0s | 9434 | 3 | 409 | 5 |
| 1d | 1 | 25.4s | 9640 | 3 | 383 | 3 |
| 2a | 2 | 18.7s | 9024 | 3 | 265 | 0 |
| 2b | 2 | 23.0s | 9599 | 4 | 280 | 1 |
| 2c | 2 | 22.0s | 9397 | 3 | 241 | 1 |
| 2d | 2 | 19.8s | 9262 | 4 | 294 | 0 |

## Reading

Accuracy is uninformative — the puzzle has one clean answer and every replica found it.

On the behavioural measures, within-set spread is comparable to between-set spread on every
dimension. Set 1 ran 290-409 words against set 2's 241-294, and set 1 referred to its beliefs
somewhat more often (0/1/5/3 vs 0/1/1/0), but with four replicas per condition these gaps sit
inside the noise. Set 1's own range on word count (119) is wider than the gap between the set
means. No claim of a belief effect is supportable from this run.

The most that can be said: every replica read its belief file, none used it to solve the puzzle,
and mentions of it were confined to procedural throat-clearing about what had been read.

## Caveat on the token counts

These are near-identical (9024-9640) because most of each budget is fixed cost — system prompt,
belief file, rules file — not reasoning. They measure the harness, not the thinking.
