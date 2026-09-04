# Editorial Guidelines for the Semantic Archaeology Lexicon

## Core Principle

Replace a common English word with the literal meaning of its
etymological roots, not its modern definition.

## Editorial Philosophy

-   Prefer **poetically active** entries over merely interesting
    etymologies.
-   Recover forgotten images rather than transparent compounds.
-   Every entry should make English briefly feel unfamiliar.

## Inclusion Criteria

1.  Common modern English word.
2.  Secure, well-attested etymology.
3.  Literal gloss is vivid, concrete, and concise.
4.  Gloss reads naturally in running prose.
5.  Surprise outweighs explanation.

## Exclude

-   Transparent compounds (churchyard, handbook, weekday).
-   Folk etymologies.
-   Acronym stories.
-   Disputed or speculative derivations.
-   Entries whose gloss adds little estrangement.

## Preferred Image Families

-   Body (little mouse, nose hole)
-   Bread & household (loaf keeper, loaf kneader)
-   Sky (wind eye, ill star, day's eye)
-   Animals
-   Salt, cattle, pebbles, hands
-   Law, religion, navigation

## Evaluation Rubric

Score each candidate on: - Philological confidence - Poetic surprise -
Frequency - Grammatical fit - Image density

Admit only consistently high-scoring entries.

## Research Method

-   Mine etymological dictionaries for 'literally...' and
    'originally...'.
-   Organize discoveries by forgotten images rather than alphabetically.
-   Keep `verified: false` until independently checked
    (e.g. Wiktionary).

## Future Scope

Keep the etymological lexicon pure. Consider a separate companion
lexicon for obsolete historical senses (e.g. awful → full of awe, silly
→ blessed).

## Recommended Repository Structure

Maintain the project as four complementary resources:

1.  **canonical.json** --- only accepted entries that meet the editorial
    standard.
2.  **candidates.json** --- promising words awaiting research and
    verification.
3.  **editorial_guidelines.md** --- the evolving philosophy, selection
    criteria, and methodology.
4.  **research_notes.md** (future) --- citations, rejected candidates,
    disputed etymologies, and reasoning.

## Suggested Entry Schema

As the lexicon grows, each entry should eventually include richer
metadata:

-   `word`
-   `gloss`
-   `etymon`
-   `language`
-   `note`
-   `verified`
-   `part_of_speech`
-   `image_family`
-   `surprise_score`
-   `frequency_score`
-   `confidence_score`
-   `wiktionary_url` (or primary verification source)

These additional fields separate philological evidence from editorial
judgment.

## Curatorial Principle

Treat the lexicon as a curated literary corpus rather than an exhaustive
etymological dictionary.

The objective is not maximum coverage, but maximum resonance. Every
substitution should justify its existence by recovering a forgotten
image that meaningfully changes the experience of reading.

When in doubt, omit the entry.

A smaller collection of remarkable recoveries is preferable to a large
collection of merely correct decompositions.

# Repository Structure

Maintain the project as three complementary resources:

1.  **canonical.json**
    -   Accepted entries only.
    -   Every entry has passed editorial review and independent
        verification.
    -   This is the production lexicon used by the electronic literature
        piece.
2.  **candidates.json**
    -   Promising words awaiting verification or editorial judgment.
    -   Includes notes about why each candidate is interesting.
    -   Serves as the research queue.
3.  **editorial.md**
    -   The evolving philosophy of the project.
    -   Documents inclusion and exclusion criteria.
    -   Records decisions, exceptions, and examples.

# Recommended Metadata

As the lexicon grows, each entry should eventually include additional
editorial metadata beyond the etymology itself:

-   part_of_speech
-   image_family (e.g. Body, Sky, Bread, Salt, Animals, Law)
-   surprise_score (1--5)
-   frequency_score (1--5)
-   confidence_score (1--5)
-   verified (initially false)
-   verification_source (e.g. Wiktionary)
-   editorial_notes

This metadata is intended for curation and quality control rather than
for presentation to readers.

# Long-Term Editorial Goal

The aim is not to create a comprehensive etymological dictionary.

The aim is to curate a lexicon of forgotten images: substitutions that
recover buried metaphors, vanished technologies, obsolete social
relations, and older ways of imagining the world.

Favor density over coverage. A smaller lexicon in which nearly every
substitution surprises the reader is preferable to a much larger one
containing many merely correct entries.

# Contested Archaeology

Not every word admits a stable reconstruction. Some of the most common
English words have been studied for generations without a scholarly
consensus about their ultimate origin.

Rather than excluding these words entirely, maintain a distinct
editorial category for **Contested Archaeology** (or **Open
Etymologies**).

The purpose of this category is not to include unverified or speculative
claims. Instead, it acknowledges that the best available scholarship has
not reached agreement.

Examples include:

-   girl
-   boy
-   bride

These entries should **not** invent a gloss. Instead, they may present
the reader with the fact of scholarly uncertainty, for example:

> origin contested

or

> scholars disagree about the original meaning

This introduces a productive interpretive tension. Most entries recover
a forgotten image or metaphor. Contested entries instead reveal the
limits of historical reconstruction, making uncertainty itself part of
the literary experience.

## Recovery Types

Maintain an internal editorial field named `recovery_type`:

-   `literal` --- direct recovery of the literal meaning of the
    etymological roots (e.g. window → wind eye).
-   `conceptual` --- recovery of an older practice or conceptual image
    (e.g. calculate → count with pebbles).
-   `semantic` --- recovery of an earlier historical sense rather than
    the root meaning (reserved for any future companion lexicon).
-   `contested` --- no scholarly consensus exists regarding the origin
    or recoverable image.

This field is primarily for editorial organization and experimentation
rather than reader-facing display.

## Editorial Principle

The project is not merely about recovering forgotten meanings.

It is about recovering forgotten images where possible, and honestly
representing the boundaries of historical knowledge where recovery is
impossible.

The lexicon should therefore communicate not only what language
remembers, but also what it has irretrievably forgotten---or what
scholars are still trying to understand.
