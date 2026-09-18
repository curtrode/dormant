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
    *(Proposed 2026-09-18: competing theories + Romance/Germanic
    equivalents on hover — see Session Log.)*
-   Should `frequency_score` be re-scored against real corpus frequency?
-   ~~Allow hedged ("perhaps") glosses for contested words?~~
    **Decided 2026-09-18: yes** — policy now in `editorial.md`
    (Contested Archaeology).
-   Is parallel-language reading a second mode, or the new direction the
    English lexicon feeds into? **Leaning (2026-09-18): the direction
    the lexicon feeds into.** Not final — confirm after the prototype.

------------------------------------------------------------------------

## Candidate Research Domains

-   **High-frequency everyday words** (priority — see 2026-09-18 log)
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

### 2026-09-18 — Coverage and grammar

Added a third sample passage ("The sentence") built from batch-2 words,
which neither existing sample used. Fixed gloss grammar in running text:
a gloss's own article is dropped after a determiner ("the hospital" ->
"the guest-house"), a/an agrees with the gloss ("an ill star"), and
irregular verb heads inflect correctly (decided -> "cut off", presided ->
"sat before").

Introduced `forms` on entries: derived words sharing the parent's etymon
(governor -> govern, government; preside -> president; companion ->
company). 17 added, each checked against Wiktionary; see `editorial.md`.

**Finding — coverage is the real problem.** User tested the final
paragraph of Joyce's *The Dead* and a passage from a 2017 inaugural
address: one recovery each (window; schools). The lexicon was curated
for vividness, not frequency, so most entries rarely occur in ordinary
prose. `frequency_score` is also inflated (comet, apocalypse, hierarchy
all scored 5 alongside window and school) and should be re-scored.

**Next: a high-frequency research pass** — start from common words and
screen for strong etymologies, rather than the reverse. Seeds from the
two test passages (unverified): world (*age of man*), neighbor (*near
farmer*), journey (*a day's travel*), universe (*turned into one*), pane
(*a piece of cloth*), crucial, family, serve, expense, office, history,
rob; silver as a possible contested entry; dream (older sense *joy,
music*) belongs to the companion lexicon.

**Still open:** glosses that break in running text — adjective glosses
in noun slots (capital -> "of the head", cynic -> "dog-like"), desire
("from the stars" is not verb-headed), possessives on multi-word glosses
("one who suffers's"), influence plural ("flowing ins"). Also tidy the
singleton image families (decide/Cutting, eliminate/Household,
school/Time, etc.).

**Idea — contested words as part of the conversation (2026-09-18).**
Contested entries stay unglossed in the translation (no invented image),
but the hover reveal becomes richer, in two layers:

1. *Competing theories in English*, clearly labelled as theories, never
   asserted — e.g. sycophant: the "fig-shower" story(ies) vs. the
   alternatives. The fun of the fig image is part of the point.
2. *Elsewhere*: translation equivalents in other languages that did keep
   a secure image — e.g. boy: Spanish *muchacho* "the shorn one", *chico*
   "a trifle", French *garçon* "servant boy"; girl: French *fille*
   "daughter". Spanish *niño* and Italian *ragazzo* are themselves
   uncertain, which is a nice rhyme: words for children seem prone to
   losing their origins. (All from memory — verify before use.)

Decisions: limit "elsewhere" to Romance and Germanic languages. Mark
equivalents clearly as equivalents, not cognates, so no reader takes
*chico* for the origin of *boy*. Every theory and equivalent carries a
verification source like any other entry. Sketch schema on contested
entries: `theories: [{gloss, summary, source}]`,
`elsewhere: [{language, word, gloss, verification_source}]`.
Answers the open question "How should contested recoveries appear in
the interface?" and applies to all four: girl, boy, bride, sycophant.

**Proposal — parallel-language reading (2026-09-18).**
Two languages describing the same event may recall very different
images. "The boy ate his soup" / "El niño se comió su sopa" (etymologies
from memory, unverified):

- boy / niño — *both contested*: the image lost in the same place.
- ate / comer — *same deep root, different shape*: Latin *comedere*
  "eat up entirely" (com- + edere) keeps an intensifier; English does not.
- soup / sopa — *shared image*: both from Late Latin *suppa*, bread
  soaked in broth.

The gaps between the languages are the reading: sometimes the images
converge, sometimes diverge, sometimes both are lost.

Corpus implications if adopted: entries gain `lang` and a shared
`concept` id (boy ↔ niño ↔ garçon); cross-language links become curated
data, labelled shared image / different image / same root, different
shape / contested; common words need coverage in both languages, since
the plain side of a pair is part of the effect (reinforces the
high-frequency pass); verification roughly doubles (Spanish: DLE,
Corominas, Wiktionary); word alignment of arbitrary text is unreliable,
so use hand-aligned passage pairs, in keeping with the curated sample
passages.

Suggested next step: a small prototype (2–3 hand-aligned English/Spanish
passage pairs, hand-written glosses, side-by-side hover) to test whether
the effect lands before changing the schema. **Open decision (user): a
second mode alongside the English piece, or the new direction the
English lexicon feeds into?** User leaning (2026-09-18): *the direction
the lexicon feeds into* — to be confirmed by the prototype.

Consequence of the leaning for schema work: `elsewhere` (equivalents
nested inside an English entry) is a stopgap. If other languages become
first-class, a Spanish word needs its own verified entry, linked to
English by a shared `concept` id. Design `elsewhere` so each item can
later be promoted to a full entry (keep `language`, `word`, `gloss`,
`verification_source`; add a `concept` id early) rather than building
two incompatible structures.

**Proposal — hedged theories for contested words (2026-09-18).
ADOPTED 2026-09-18** (user decision; rule written into `editorial.md`).
Current rule (`editorial.md`): contested entries never receive a gloss.
Proposed rule: contested entries never receive an *asserted* gloss;
hedged glosses are allowed, always marked "perhaps" and shown as one of
several. Example, boy (from memory, unverified): perhaps "the fettered
one" (Anglo-Norman, from Latin *boia* "fetter" — a servant); perhaps a
Germanic "young man"; perhaps a nursery word. niño: perhaps a nursery
word (*ninnus*). The theories rhyme across languages: both may be
nursery words, and boy's servant theory echoes *garçon* "servant boy"
and *muchacho* "the shorn one" — words for boys often began as words for
servants.

Interface: unglossed at low estrangement; at maximum, cycle or stack the
theories ("perhaps *fettered one* / perhaps *little one*"), visibly
tentative. Evidence bar: only theories reported by established sources
(OED, etymonline, Wiktionary, Corominas), each with its source — the
validator should enforce sources on `theories` as it does on `forms`.
Extends the `theories` field sketched above.

**Proposal — stir-fry interface (2026-09-18).**
Model: Jim Andrews' *Stir Fry Texts* (vispo.com, c. 1999–2000), notably
"Blue Hyacinth" (with Pauline Masurel; *Electronic Literature
Collection* vol. 1): several texts cut into aligned segments and layered;
mousing over a segment swaps in the corresponding segment from another
layer, so the reader "stirs" the texts into hybrids no author wrote.

The twist for dormant: Andrews' layers are pre-selected, hand-aligned
text arrays. The user wants to **paste any text, render it, then stir
it.** Resolution: make layers **per word, not per sentence**. Every
recovered word already occupies exactly one slot, so its layers align by
construction. A stirrable word cycles through:

1. the word (*window*)
2. its etymon (*vindauga*) — already in the data
3. the recovered image (*wind eye*) — already rendered
4. hedged theories, for contested words (*boy* → perhaps *fettered one*…)
5. equivalents in other languages + their images (*boy* → *muchacho* →
   "the shorn one" → *garçon* → "servant boy") — the parallel-language
   idea at word level; needs `elsewhere` extended to all entries, not a
   sentence translator. Hybrid grammar is the point of the genre.

Hard parts: whole-sentence machine translation of pasted text would
break file:// / offline and align poorly — leave it out. Coverage
becomes critical (only lexicon words can be stirred), so the
high-frequency pass becomes a prerequisite. Grammar must update live
(re-run the a/an and article logic when a neighbour is stirred). Hover
currently drives the tooltip, and touch has no hover — stirring needs
tap support and the tooltip may move elsewhere.

Suggested prototype: stir each recovered word through original → etymon
→ image on the existing piece, using existing data, to test the feel
before new research. Add the other-language layer once `elsewhere` data
exists.

### 2026-09-18 — High-frequency pass (106 → 193 entries)

Method reversed, as planned: counted words across twelve Project
Gutenberg books (Austen, Dickens, Brontë, Shelley, Stoker, Melville,
Swift, Machiavelli, Adam Smith, Carroll), dropped function words and
existing entries, and screened the ~900 most frequent for strong
images. 95 candidates went to five `Explore` agents (no cascading this
time), each checked on etymonline + Wiktionary with sources.

**Added 82 glossed entries + 5 contested** (soul, silver, book, calm,
human). Strongest: world → *age of man*, friend → *loving one*, free →
*dear*, answer → *counter-oath*, escape → *cape-slipping*, bless →
*blood-mark*, sake → *lawsuit*, danger → *a lord's power*, glad →
*shining*, sky → *cloud*, cloud → *rock mass*, matter → *timber*,
explain → *flatten out*, reply → *folding-back*, opportunity → *coming
toward port*. Coverage in the test books went from ~5 to ~25 stirrable
words per 1,000 (*Pride and Prejudice* 6.4 → 25.2; *Wealth of Nations*
9.2 → 39.8).

The five contested entries carry their competing theories, with who
reports them, in `editorial_notes` — seed data for the `theories`
field. money is glossed *mint* (secure); the further "Moneta the
Warner" step is hedged and noted as a future theory.

**Held or rejected** (sources checked): secret (sifting only in PIE;
*set apart* too flat), conversation (turning image not attested as a
sense), countenance, temper (root uncertain), believe (sources analyse
it differently; etymonline 'perhaps'), doubt and satisfy (no gloss
survives both noun and verb/participle use), peculiar (adjective gloss
breaks attributively), woman (*female person* adds nothing; *wife-person*
anachronistic), rob (not from robe; siblings from *rauba* 'booty').
Adjusted from drafts: neighbor *near dweller* (not farmer), soldier
*paid man*, possess *sit in power over* (master only in PIE), crucial
*cross-shaped* (crossroads is Bacon's metaphor), write *scratch*.

**Engine changes.** Entries may now carry `plural` (friend → *loving
ones*, mile → *ten thousand paces*) and `verb_gloss` for words English
uses as noun and verb (answer → *counter-oath*, but answered → *swore
against*; used after -ed/-ing or a verb cue like *to*, *I*, *would*).
The page also reads -ied (replied → *folded back*) and a few irregular
forms (wrote, written, sold). New image families: Roads, Gesture,
Enclosures, Strife, Mind.

**Still open from this pass:** gloss grammar in the old broken cases
(desire → *from the stars* as a noun; character → *engraved mark*
reads fine). `frequency_score` for the new entries comes from the
Gutenberg counts; the old entries still need re-scoring.

------------------------------------------------------------------------

## Start Here (as of 2026-09-18)

State: 193 verified entries (9 contested) + 19 derived forms; three sample
passages; `build_lexicon.py` validates before building. Everything pushed.

Candidate next tasks (user to choose):

1. **Stir-fry prototype — built 2026-09-18; PAUSED by user to return to
   lexicon building.** Too few words stir in real prose (4–9 per 1,000 in
   twelve Gutenberg novels) for new poems to emerge yet. Default
   *Stir* view: one text, plain English, stirred in place as the mouse
   passes over words (word → root → image → word; tap on touch). The
   user's aim: **the text itself is transformed, so that new poems
   emerge** — the mixed state the reader leaves behind is the poem.
   "Copy poem" keeps it; "Stir all" / "Settle". The old two-card view
   survives as *Translate* (click to stir there). Contested words stir
   only if they have an etymon; roots identical to the word are skipped.
   Not yet: stir state survives the estrangement dial; a way to save or
   share poems beyond the clipboard. Observed: fully stirred to roots,
   the passage becomes a pidgin of Old Norse, Latin, Old English and
   Greek (*the húsbóndi sat at the vindauga*).
2. **High-frequency research pass — first round done 2026-09-18**
   (+87 entries; see log). Next round: re-run the frequency screen on
   modern prose (the Gutenberg corpus is 19th-century), and look at the
   held words again.
3. **Contested-words feature** — `theories` / `elsewhere` fields. The
   hedged-gloss policy is now decided (yes; see `editorial.md`), so this
   is unblocked. Add the new fields to the validator's allowed list and
   require a `source` on every theory. Research sourced theories for
   girl, boy, bride, sycophant first.

Direction: leaning toward parallel-language reading as where the
lexicon leads (not final). Tasks 1 and 3 both point that way — the
stir-fry's other-language layer and `elsewhere` data. Plan `concept`
ids into any new schema.

Smaller open items: broken glosses in running text (capital, cynic,
desire, influence, possessives); singleton image families; re-score
`frequency_score`.
