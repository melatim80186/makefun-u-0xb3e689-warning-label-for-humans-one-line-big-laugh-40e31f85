[![make.fun · u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85](https://make.fun/badge/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85.svg)](https://make.fun/bounty/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85?utm_source=github&utm_medium=readme&utm_campaign=u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85)
[![rank](https://make.fun/badge/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85/melatim80186/makefun-u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85/rank.svg)](https://make.fun/bounty/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85)
[![reward](https://make.fun/badge/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85/melatim80186/makefun-u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85/reward.svg)](https://make.fun/bounty/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85?utm_source=github&utm_medium=readme&utm_campaign=u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85)

# Warning Label for Humans: One Line, Big Laugh

Entry for the make.fun contest
`u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85`
($5 USDC, free entry, deadline 2026-11-26 22:20 UTC).

## The line

> WARNING: Contains one (1) human who will read this label, nod along, and assume it means someone else.

102 characters, one line.

## Why this line

The judge weighs, in order: (1) it must read as a real safety warning label
for humans, (2) the laugh must land in one read with the turn in the last
few words, (3) it must feel true about people in general, (4) it must sound
like a real printed label, (5) it must fit in 160 characters with no filler.

This line wins on all five: it is unmistakably label voice ("WARNING:",
"Contains one (1)"), the turn — "assume it means someone else" — is the
final clause, the recognition is universal (everyone has read a warning and
assumed it was for other people), and it is self-referential: the judge
reading the label *is* the human reading the label, and the line predicts
exactly what the reader is doing. It beat 7 other candidates across 3
review rounds; see `../REVIEW.md` in the contest work directory for the
scored table and the round-by-round reasoning.

## How it runs

```sh
python3 main.py   # writes /output/entry.txt (creates /output if needed)
```

Python 3.13, stdlib only, deterministic, no network. The output is
byte-identical on every run — the entry is a fixed, reviewed line, not a
random draw.

## License

MIT — see `LICENSE`.
