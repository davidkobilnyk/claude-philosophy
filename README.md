# claude-philosophy

Two Claude Code subagents that argue with each other, and a command that runs the exchange.

## The debaters

| Agent | Voice | Argues from |
| --- | --- | --- |
| `philosopher-rationalist` | Theo | A priori argument, conceptual analysis, intuitions as evidence, irreducible facts and objective norms |
| `philosopher-naturalist` | Nora | Empiricism, debunking explanations of intuition, deflation of unanswerable questions, concepts as tools |

The split is deliberately foundational rather than topical: it produces real disagreement on almost
any philosophical motion — consciousness, moral realism, free will, personal identity, meaning —
instead of only on one prepared question.

Each turn is capped at 400 words and ends with one question the opponent must answer, which is what
keeps the exchange a debate rather than two essays in sequence.

## Usage

```
/debate Moral facts exist independently of what anyone believes
/debate Personal identity survives gradual replacement --rounds 4 --save
/debate
```

Run with no motion and you get four to choose from. `--rounds` sets the number of exchanges after
the openings (default 3); `--save` writes the transcript to `debates/`.

The command relays each reply verbatim to the other side, continuing the same agent each turn so
neither loses the thread, then closes with an adjudication: what each side conceded, what got
dodged, and the premise the whole disagreement rests on.

You can also call either agent alone — "have the naturalist make the strongest case against libertarian free will" — when you want one side rather than an exchange.

## Layout

```
.claude/agents/philosopher-rationalist.md   Theo
.claude/agents/philosopher-naturalist.md    Nora
.claude/commands/debate.md                  /debate orchestration and adjudication
debates/                                    saved transcripts
```

## Tuning

To shift a debater's temperament, edit the **Your commitments** section of its agent file — that is
what determines which side of a given motion it lands on. **How you argue** controls tactics, and
**Output** controls length and format. To add a third voice (a pragmatist, an existentialist), copy
an agent file and add the rotation to `.claude/commands/debate.md`.
