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
- Disputed or speculative derivations without scholarly support
  (contested words with sourced competing theories are handled under
  Contested Archaeology).
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
entries **never receive an asserted gloss**. At most they may carry
*hedged* glosses (see below); otherwise they present the reader with the
fact of uncertainty:

> origin contested

or

> scholars disagree about the original meaning

Current examples: **girl**, **boy**, **bride**, **sycophant**.

Where most entries recover a forgotten image, contested entries reveal
the limits of historical reconstruction — making uncertainty itself part
of the literary experience.

**Hedged glosses (decided 2026-09-18).** A contested entry may carry
glosses for the competing theories, provided that each one:

- is marked **"perhaps"** wherever it appears, and is never shown as the
  only reading — always one of several, visibly tentative (boy → perhaps
  *fettered one* / perhaps *little one*);
- is reported by an established source (OED, etymonline, Wiktionary,
  Corominas), and that source is recorded with the theory;
- never appears in the text as first rendered; hedged glosses surface
  only when the reader stirs the word, or in the reveal.

A theory we cannot source is left out, however good the image. This is
the one exception to "Disputed or speculative derivations" under
Exclusion Criteria: the theories are admitted as theories, never as the
word's origin.

**Planned: contested words as conversation.** A contested entry's reveal
may offer two things:

- *Competing theories* in English, carrying the hedged glosses above
  (sycophant's fig-shower stories).
- *Elsewhere*: equivalents in Romance and Germanic languages that kept
  a secure image (boy → Spanish *muchacho* "the shorn one", *chico*
  "a trifle"). These are marked as equivalents, not cognates or origins.

Both require a verification source like any other entry. See the
2026-09-18 entry in `research_notes.md` for the proposed schema.

## Preferred Image Families

- Body (little mouse, nose hole)
- Bread & household (loaf keeper, loaf kneader)
- Sky (wind eye, ill star, day's eye)
- Animals
- Salt, cattle, pebbles, hands
- Horses, kinship
- Law, religion, navigation, agriculture
- Medicine, trade, textile, measurement (added in the second research pass:
  clinic, budget, tally, symbol)
- Geography, water, theater, knowledge (rival, trivial, person, encyclopedia)
- Roads, gesture, enclosures, strife, mind (high-frequency pass: trodden
  path, standing-around, enclosed yard, confusion, carefree)
- Chance, names, trees (modern-prose pass: fall of the dice, Fawkes
  effigy, bark-store)

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
- `forms` (optional) — derived words that share the entry's etymon and
  image (governor → *govern*, *government*). Each form gives its own
  `word`, `gloss`, `part_of_speech` and `verification_source`, with
  optional `plural` and `surprise_score` overrides; everything else is
  inherited. Admit a form only if the parent's image survives in it.
- `plural` (optional, nouns) — the gloss's plural when the last word
  cannot simply take -s (friend → *loving ones*).
- `verb_gloss` (optional, non-verbs) — the gloss used when the word is
  used as a verb (answer → *counter-oath*; answered → *swore against*). Where
  no verb image is attested, use the noun gloss itself as a verb (focus →
  *hearth*, focused → *hearthed*); this adds no etymological claim.
- `theories` (planned; contested entries only) — competing theories,
  each with a hedged `gloss`, a `summary` and a `source`.
- `elsewhere` (planned) — Romance and Germanic equivalents, each with
  `language`, `word`, `gloss` and `verification_source`.

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
