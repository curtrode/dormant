# Editorial Guidelines — Semantic Archaeology Lexicon

## Core Principle

Replace a common English word with the literal meaning of its
etymological roots, not its modern definition. The substitution is not a
definition; it is an attempt to awaken a dormant image (window → *wind
eye*, mortgage → *death pledge*).

## Editorial Philosophy

- Prefer **poetically active** entries over merely interesting
  etymologies.
- Recover forgotten images rather than transparent compounds.
- Every entry should make English briefly feel unfamiliar.
- Correctness is a constraint; estrangement is the goal.

## Inclusion Criteria

1. Common contemporary English word.
2. Secure, well-attested etymology.
3. Literal gloss is vivid, concrete, and concise.
4. Gloss reads naturally in running prose.
5. Surprise outweighs explanation.

## Exclusion Criteria

- Transparent compounds (churchyard, handbook, weekday).
- Folk etymologies.
- Acronym stories.
- Disputed or speculative derivations without scholarly support.
- Entries whose gloss adds little estrangement.

When in doubt, omit the entry. A smaller collection of remarkable
recoveries is preferable to a large collection of merely correct
decompositions.

## Recovery Types

Each entry carries an internal `recovery_type` field for editorial
organization (not reader-facing):

- `literal` — direct recovery of the literal meaning of the roots
  (window → wind eye).
- `conceptual` — recovery of an older practice or material image
  (calculate → count with pebbles).
- `semantic` — recovery of an earlier historical sense rather than the
  root meaning (reserved for a future companion lexicon).
- `contested` — no scholarly consensus exists regarding the origin.

## Contested Archaeology

Not every word admits a stable reconstruction. Some of the most common
English words have been studied for generations without consensus about
their ultimate origin. Rather than excluding them, maintain a distinct
**Contested Archaeology** category.

The purpose is not to admit speculative claims, but to acknowledge that
the best available scholarship has not reached agreement. Contested
entries **do not** receive an invented gloss. Instead they may present
the reader with the fact of uncertainty:

> origin contested

or

> scholars disagree about the original meaning

Current examples: **girl**, **boy**, **bride**.

Where most entries recover a forgotten image, contested entries reveal
the limits of historical reconstruction — making uncertainty itself part
of the literary experience.

## Preferred Image Families

- Body (little mouse, nose hole)
- Bread & household (loaf keeper, loaf kneader)
- Sky (wind eye, ill star, day's eye)
- Animals
- Salt, cattle, pebbles, hands
- Horses, kinship
- Law, religion, navigation, agriculture

Organize discoveries by these forgotten images rather than
alphabetically.

## Evaluation Rubric

Score each candidate on:

- Philological confidence
- Poetic surprise
- Frequency in contemporary English
- Grammatical fit
- Image density

Admit only consistently high-scoring entries.

## Research Method

- Mine etymological dictionaries for "literally…" and "originally…".
- Keep `verified: false` until independently checked (e.g. Wiktionary,
  etymonline, OED).
- Record the verification source on every accepted entry.
- Log rejected candidates and disputed etymologies in
  `research_notes.md`.

## Entry Schema

Each entry should include:

- `word`
- `gloss`
- `etymon`
- `language`
- `note`
- `part_of_speech`
- `image_family`
- `recovery_type`
- `surprise_score` (1–5)
- `frequency_score` (1–5)
- `confidence_score` (1–5)
- `verified`
- `verification_source`
- `editorial_notes`

This metadata separates philological evidence from editorial judgment
and is intended for curation rather than reader-facing display.

## Repository Structure

The project is maintained as a set of complementary resources:

1. **canonical.json** — accepted, independently verified entries. The
   production lexicon used by the electronic literature piece.
2. **candidates.json** — the research queue: promising words awaiting
   verification or editorial judgment, with notes on why each is
   interesting.
3. **editorial.md** — this document: philosophy, inclusion/exclusion
   criteria, and methodology.
4. **poetics_of_semantic_archaeology.md** — the conceptual essay.
5. **research_notes.md** — laboratory notebook: observations, open
   questions, rejected candidates, and disputed etymologies.
6. **semantic_archaeology_strongest_entries.md** — legacy source
   snapshot, now superseded by `canonical.json`.

## Future Scope

Keep the etymological lexicon pure. Consider a separate **companion
lexicon** for obsolete historical senses (e.g. awful → *full of awe*,
silly → *blessed*), which would use the `semantic` recovery type.

## Curatorial Principle

Treat the lexicon as a curated literary corpus rather than an exhaustive
etymological dictionary. The objective is not maximum coverage but
maximum resonance.

Recover forgotten images where possible, and honestly represent the
boundaries of historical knowledge where recovery is impossible. Favor
density and surprise over coverage. Every substitution should justify its
existence by recovering a forgotten image that meaningfully changes the
experience of reading.
