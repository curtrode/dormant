# Research Notes

This document is intentionally informal. It records observations, open
questions, editorial decisions, rejected ideas, and promising avenues of
investigation. It is a laboratory notebook rather than a polished
document.

------------------------------------------------------------------------

## Core Observation

The project is not collecting interesting etymologies.

It is collecting **forgotten images** that can be reactivated in
contemporary reading.

The central editorial question is therefore:

> Does this substitution make the sentence more interesting to read?

Correctness is a constraint. Estrangement is the goal.

------------------------------------------------------------------------

## Emerging Editorial Criteria

The strongest entries tend to:

-   recover a concrete image rather than an abstract meaning
-   reconstruct a historical practice rather than merely decompose a
    compound
-   read naturally in running prose
-   surprise even well-read readers
-   remain philologically conservative

------------------------------------------------------------------------

## Possible Evaluation Axes

-   Philological confidence
-   Poetic surprise
-   Frequency in contemporary English
-   Grammatical fit
-   Image density
-   World-building potential

The last criterion is especially promising. Some substitutions briefly
reconstruct an entire historical world.

Examples:

-   calculate → count with pebbles
-   candidate → clothed in white
-   salary → salt money
-   gossip → god sibling

------------------------------------------------------------------------

## Image Families

Recurring conceptual domains include:

-   Bread
-   Animals
-   Body
-   Hands
-   Eyes
-   Salt
-   Pebbles
-   Stars
-   Horses
-   Kinship
-   Law
-   Navigation
-   Agriculture

Future research should be organized by these image families rather than
alphabetically.

------------------------------------------------------------------------

## Contested Archaeology

Some words should never receive a reconstructed gloss because no
scholarly consensus exists.

Examples currently include:

-   girl
-   boy
-   bride
-   sycophant (competing fig-gesture / fig-informer theories, no consensus)

These are not failures of research but evidence of the limits of
historical knowledge.

------------------------------------------------------------------------

## Open Questions

-   Are verbs ultimately more powerful than nouns?
-   Should adjectives receive higher editorial priority?
-   How should adverbs be handled?
-   Should semantic archaeology (obsolete senses) remain a separate
    companion project?
-   How should contested recoveries appear in the interface?

------------------------------------------------------------------------

## Candidate Research Domains

-   Roman law
-   Astronomy
-   Medieval religion
-   Domestic life
-   Agriculture
-   Navigation
-   Medicine
-   Textile production
-   Trade and finance
-   Measurement and mathematics

------------------------------------------------------------------------

## Working Principle

Recover forgotten images where possible.

Represent the limits of historical knowledge where necessary.

------------------------------------------------------------------------

## Session Log

### 2026-09-03 — Reactivation

Project was found dormant: `canonical.json`/`candidates.json` empty, 27
finished entries stranded in a markdown file, two contradictory editorial
docs. Migrated the 27 entries (plus three contested seeds: girl, boy,
bride) into the full schema, verified every one against
Wiktionary/etymonline, scored `surprise`/`frequency`/`confidence`, and
promoted 31 verified entries into `canonical.json`. Consolidated the
duplicate editorial docs into one `editorial.md`. Retired the legacy
snapshot file.

Built the electronic-literature piece (`index.html` + `build_lexicon.py`
+ `lexicon.js`): parallel translation/original cards, a hover-linked
tooltip showing the source word + etymon, and an "estrangement" dial that
sets the surprise threshold for which words fire. Contested entries
surface only at maximum intensity, marked but never glossed. Fixed gloss
inflection so tense/number agree with the surface word (`calculated` →
"counted with pebbles", not "count with pebbles").

### 2026-09-04 — Deepening (31 → 106 entries)

User reported that two arbitrary test passages produced zero recoveries —
expected, since only ~7 of the 31 words were common enough to appear in
ordinary prose. Ran a second research pass across five domains (Latin
abstractions, Greek, sky/mind/medicine, trade/textiles/measurement,
law/religion/politics), each independently verified against
Wiktionary/etymonline. Added 75 entries after applying the editorial bar
(dropped `senate`, `pontiff`, `sacrament`, `sacrifice`, `veto`, `vertigo`,
`phlegmatic` for low surprise or shaky sourcing). `sycophant` was added as
a fourth **contested** entry (gloss: null) rather than asserting the
disputed "fig-shower" story as fact.

Target scale had been "medium, ~40-60 new entries" but the Greek batch
alone was strong enough that the final total (75 new) overshot that on
purpose rather than discarding good material — flagged to the user rather
than silently exceeding scope.

**Not yet done: the body/animals/plants domain.** Two attempts both
failed for process reasons (see below), not for lack of good material —
the seed list (dandelion, pupil, vaccine, lunatic, dexterous, sinister,
pedigree, squirrel, porpoise, walrus, tulip, chameleon, tadpole,
cockroach, mongoose, etc.) is still untried. This is the natural next
research batch.

**Process lesson — agent delegation cascades.** Dispatching six
`general-purpose` research agents in parallel caused several to
self-appoint as orchestrators: instead of doing the research themselves,
they spawned child sub-agents and then reported back "waiting for
background agents" with no data. Re-dispatching the same domains as
`Explore`-type agents (which have no `Agent` tool and therefore cannot
delegate) fixed it reliably. **For future research fan-outs in this
project, prefer `Explore` over `general-purpose`** when the task is
"search the web and return structured findings" — it cannot cascade.

Other domains worth running next, per the candidate list above: medieval
religion (beyond what law/religion covered), navigation (beyond
governor/arrive), measurement and mathematics (beyond tally/examine),
and the still-open body/animals/plants batch.
