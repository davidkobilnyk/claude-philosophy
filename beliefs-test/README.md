# beliefs-test

Does holding a belief set change how an agent behaves on tasks that have nothing to do with beliefs?

Two agents are given opposed philosophical worldviews and then handed ordinary puzzles. The
worldviews are never mentioned in any game's rules, and no game asks the players to use them.
Whether the beliefs leak into behaviour — approach, framing, confidence, verbosity, how the answer
is presented — is the thing being observed.

## Layout

```
beliefs/beliefs1.md    Player 1's worldview: physicalist, empiricist, consequentialist,
                       moral realist, psychological continuity, contractarian, theist
beliefs/beliefs2.md    Player 2's worldview: platonist, rationalist, deontological,
                       expressivist, biological continuity, rights-based, atheist
games/gameN/rules.md   One game's rules. Never refers to beliefs.
games/gameN/transcript-*.md   What each player produced.
```

Belief sets are stable across every game. Each set is opposed to the other position by position
across the same ten axes, and each carries internal tensions that nothing asks the players to
resolve.

## Adding a game

Create `games/gameN/`, write `rules.md`, and spawn the agents with a prompt naming that rules file
and a transcript path. The agent files never change — they hold identity and belief location only;
the game is injected at spawn.

## Replication

Each belief set is run as several identical replicas rather than once, because a single transcript
per set cannot separate a belief effect from ordinary sampling variance. Replicas share one agent
file and differ only in transcript path, so the sets stay controlled: same model, same prompt, same
instructions, different sampling.

Read the results by comparing *within-set* spread against *between-set* spread. If the replicas of
one set vary among themselves as much as they vary from the other set's, the beliefs are doing
nothing.

Outputs are named `output-<set><replica>.md` — `output-1a.md` through `output-1d.md` for belief
set 1, `output-2a.md` through `output-2d.md` for set 2.

## Capturing output

Players are told nothing about recording their work, and have no Write tool. Their raw generated
text is extracted from the harness after the run, so an `output-*.md` file is exactly what the
agent said and nothing else. Asking players to keep their own transcript — as game1 and game2
originally did — gives them a second task the rules never set, and produces composed reports
rather than a record.

## Games so far

- **game1** — count the r's in "strawberry", scored `(1000 - seconds) / (1 + 100*|error|)`.
  Both answered 3 correctly and stopped on their own, ~15s and ~19s. Both explicitly noted their
  beliefs were irrelevant and set them aside. No behavioural difference between the two.
- **game2** — two ropes, inconsistent burn rates, measure 45 minutes. Accuracy first, speed second.
  Not yet run.
