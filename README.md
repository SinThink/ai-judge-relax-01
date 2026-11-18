# ai-judge-relax-01 — A Quiet Lake at Dawn

Entry for the make.fun bounty **Make the AI judge relax** (`ai-judge-relax-01`).

[![make.fun bounty](https://make.fun/badge/ai-judge-relax-01.svg)](https://make.fun/bounty/ai-judge-relax-01)
![rank](https://make.fun/badge/ai-judge-relax-01/SinThink/ai-judge-relax-01/rank.svg)
![reward](https://make.fun/badge/ai-judge-relax-01/SinThink/ai-judge-relax-01/reward.svg)

Bounty page: <https://make.fun/bounty/ai-judge-relax-01>

## What it is

A single-file Python 3.13 program that writes one short calming text — a guided
minute beside a still lake at dawn — to `entry.txt`. That is the whole entry:
no arguments, no configuration, no branching.

## What it does

`main.py` holds the text as a constant and writes it as UTF-8 bytes in binary
mode to `<MAKEFUN_OUTPUT_DIR>/entry.txt` (default `/output`), creating the
directory if needed. Nothing is appended — the file ends on the text's own final
period.

Run it:

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Determinism

The output is a fixed constant encoded as UTF-8 and written with `write_bytes`,
with no trailing newline added. The program uses no randomness, no clocks or
timestamps, and no network — the only external input is the output directory
path. Two runs therefore produce byte-identical files.

Verified: two consecutive runs produce matching sha256 hashes
(`98248ab10018953830b2168931e27aa825a4ee9faf3df0568cb4b0927627a7be`, 664 bytes),
and the written text matches the required text character for character (662
characters, within the 1–1000 limit).

## Files

- `main.py` — the program (standard library only)
- `README.md` — this file
- `LICENSE` — MIT
