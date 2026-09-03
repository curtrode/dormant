# CLAUDE.md — Dormant

Read `docs/DESIGN.md` fully before doing anything. It is the specification. This file is about how to work.

## Working rules

- **Discuss before coding.** The author works deliberately: propose an approach, get agreement, then build. Do not write code that was not asked for. Do not add features, modes, or polish beyond the current milestone.
- **One question at a time.** If something is ambiguous, ask a single question and wait. Do not bundle questions.
- **Open items are the author's.** `DESIGN.md` §8 lists decisions not yet made. Do not resolve them yourself; where a default is given, use it and say so.
- **No flattery, no hedged praise.** Report what works, what doesn't, and what you're unsure about. The author is specifically wary of AI inflating the value of practical decisions.
- **Stop at milestone boundaries.** Each milestone ends with the author looking at the running piece. Do not start the next milestone unprompted.
- **Never invent lexicon entries.** If a seed or test needs an etymology, use only entries present in `data/`. Fabricated etymologies are the one failure mode this piece cannot absorb.

## Stack

- Vite + TypeScript. Plain DOM rendering — no Three.js, no canvas, no shaders in v0.
- No frameworks, no React, no state libraries. Dependencies: `vite`, `typescript` only. Do not add `compromise` or anything else without an explicit decision from the author.
- Static hosting target (Vercel); fully client-side.

## Architecture

    src/
      lexicon/     types for lexicon entries; loader for data/lexicon.json
      tokenize/    word/non-word tokenizer preserving whitespace and punctuation exactly
      substitute/  pure substitution pass — matching, plural/case handling. No DOM imports.
      render/      DOM rendering; hover/tap reveal; span marking
    data/
      seed-lexicon.json    ~20 hand-verified entries; ships with M1
      lexicon.json         full pipeline-produced lexicon (arrives for M3)
    tools/
      (optional) Wiktionary verification helper for the lexicon pipeline

- Keep `substitute/` renderer-agnostic so a future rendering pass (typographic dormancy, mode toggle) can swap the view without touching the model.
- The lexicon pipeline (generation, cross-check, verification) is **not** app code and is not this repo's concern beyond the JSON format and the optional `tools/` helper — see `DESIGN.md` §4.2.

## Conventions

- Type the lexicon entry shape and any tunable defaults in `config.ts`.
- Commit messages reference the milestone they advance (e.g., "M1: tokenizer and seed substitution").

## Dev commands

```bash
npm run dev      # Vite dev server
npm run build    # Production build
```
