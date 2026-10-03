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

### 2026-09-18 — Modern-prose pass (193 → 288 entries)

The first pass used 19th-century novels, so this one screened the
6,000 most frequent words in `wordfreq` (Speer et al.: subtitles, news,
Wikipedia, web, social media) that were not yet in the lexicon. 96
candidates, five `Explore` agents, etymonline + Wiktionary for each.

**Added 94 glossed entries + 1 contested** (religion: Cicero's
*relegere* 're-read' against the later *religare* 'bind back'). Words
the novel corpus could not have surfaced: video → *I-see*, guy →
*Fawkes effigy*, phone → *far voice*, data → *given things*, kid →
*young goat*, worry → *strangle*, nice → *not-knowing*, sad → *sated*,
smart → *stinging*, weird → *fateful*, bus → *for-all*, gas → *chaos*,
map → *world-cloth*, dollar → *valley coin*, cancer → *crab*, library →
*bark-store*, test → *assay pot*, average → *cargo damage*, check →
*king*. Modern coverage (wordfreq-weighted, all entries firing): 21.0 →
40.3 recoverable words per 1,000.

**Held:** place (the verb 'placed' leaves *broad street*
ungrammatical), island (the water image is only Proto-Germanic), fan
(fanatic 'temple-mad' only 'probably'). **Adjusted from drafts:**
economy *household management* (not 'law'), credit *thing entrusted*
(not 'believed'), phone *far voice* (a clipping of telephone), photo
*light-writing*, travel *toil* (the tripalium torture story is
disputed), theory *looking-at*, weird *fateful*, education *rearing*
('draw out' is a popular misreading).

**Policy used:** where a noun gloss has no attested verb, the verb gloss
is the same noun used as a verb (focus → *hearth* / *hearthed*; score →
*notch*; check → *king*). This makes no new etymological claim.
Page: recognizes 'paid' and verb cues like *don't*; new irregular pasts
(struck, went). New image families: Chance, Names, Trees.

### 2026-09-18 — Estrangement dial removed

User asked whether the dial was necessary. With 288 entries it had
become nearly vestigial: settings 3–5 fired 275–278 of 278 glossed
entries, so only 'faint' and 'low' did anything, and they only thinned
an already sparse effect (~40 words per 1,000). In the Stir view it
duplicated the reader's own hand, reduced the possible poems, and
wiped the reader's stirring whenever it moved. Removed. Every lexicon
word now renders and stirs; contested words appear in every view
(marked in Translate, plain in Stir, stirrable only if they have an
etymon). `surprise_score` stays as editorial data — a possible use:
order "Stir all" so the strongest images turn first. The hedged-gloss
rule in `editorial.md` now says theories surface only when the reader
stirs the word or opens the reveal.

### 2026-09-26 — Homonym collection begun

A separate chat session (handoff in `homonyms/homonyms_handoff.md`)
proposed a standalone **homonym collection**. The idea is that one
spelling can hold unrelated pasts (mint → *Juno's warning-temple* / *the
herb*), and the piece presents both instead of choosing one. It comes
with a drafted **Homonymous Archaeology** clause for `editorial.md`, not
yet added. This session regenerated the 1,560-word candidate list
(`find_homonym_candidates.py`, from droher/etymology-db, Zipf ≥ 3.0).
It then cut the list with `filter_homonym_candidates.py`, which reads
each word's Wiktionary page. A word stays when it has two or more
numbered etymologies with current senses that descend from different
roots. 1,560 → 374 (`dormant_homonym_shortlist.csv`). Every known
homonym survives (bank, mint, grave, school, sound, date, host, quarry,
policy, fair, temple, bark, fan, guy). Pupil, minute, kind and salary
drop out, correctly, as one root each. Cleave is still missing: it
never made the candidate list. Noise remains for the hand cull (*on*,
*son*, *mother*, *media*, *house*).

User is marking keep / maybe / reject on a review page
(https://claude.ai/artifact/ShrW4a4jZmLZUWAjBn2kVZ; marks are kept in
the page's `marks` database). Also discussed: slang is admissible under
the existing criteria. It usually fails on secure etymology, but *kid*
and *guy* are already in; *pal*, *chum*, *boss*, *booze*, *jeans* and
*buck* are candidates. Sense-flip slang (*sick*, *wicked*) is out,
because it has no buried image.

------------------------------------------------------------------------

### 2026-09-29 — Constraint-writing idea (recorded)

User idea: a composition mode. The user writes a text (for example, a
12-line poem) under a constraint: every line must contain one or more
lexicon words. The words come either from the whole lexicon or from a
random draw of lexicon words dealt to the writer. It is an Oulipian
turn: the lexicon becomes a word bank to write *with*, not only a lens
to read through. Not yet designed or built. Open questions: how many
words per line; does the draw fix the words or only the pool; does the
finished poem then stir (so each required word surfaces its buried
image); and are lines validated live as the writer types.

Prototype built the same day: `docs/write.html` (engine shared with
`index.html` through `docs/stir.js`). First findings from the user's
own writing:

- The Whole lexicon rule is too loose. Lines hold three to five words
  without trying; even *line* is an entry.
- A writer who knows the lexicon writes *toward* the images (*window*,
  *trade winds*, *library of gusts* all lean on *wind eye*). That gives
  two modes: knowing the images, the writer plants a second poem under
  the first, like a pun or a cipher; not knowing them, the stir
  surprises the writer too and the lexicon co-writes. A tap-to-turn
  peek on hand cards was built and then removed at the user's call:
  no peek for now; the hand stays blind.
- Homonym hand sketched in chat and **paused** by the user. Open
  choices recorded for later: which ghost the stir surfaces (the unused
  sense, both tangled, or a cycle through both); homonyms as rare cards
  (2–3 per hand) rather than a whole hand; an honour-rule variant that
  uses the word in both senses. A prototype would use a small draft
  data file in `docs/`, leaving `canonical.json` and the duplicate-word
  rule untouched. The review page had no marks saved as of 2026-09-29.
- Ghosts, not only replacements: the finished poem now opens in a
  *Bleed* view ported from `homonyms/dormant-bleed-study.html` (the
  poem stays as written; images rise above the words). Every lexicon
  word bleeds. Ghosts from the hand ("called") rise first; others
  ("uninvited") rise last, one by one, fainter. The user wanted these
  inadvertent ghosts. Replacement stays as the second view, *Stir*.

### 2026-10-02 — Root families (idea recorded)

User question: *draft* is not in the homonym corpus (correctly: it is
polysemy, one word with many senses), nor in the lexicon. Its senses all
descend from Old English *dragan* "to drag, pull": a draft of air, a
draught of beer, the draft of an essay, the military draft, a draft
horse, a bank draft, a ship's draft. *Draw a picture* hides the same
pull: a line is a stylus dragged across a surface.

The idea: a draft of wind can *summon* the dragged stylus. These are
siblings, not layers. Neither contains the other; they are two branches
of one root. The lexicon cannot express this yet: every entry stands
alone, and no two of the 288 canonical entries share an etymon.

Two directions, kept distinct:

- **Depth** (already practised): one word's chain of images, e.g. write
  *score* → Proto-Germanic *tear, scratch*. Deeper links are cut when
  hedged (thing, *tenk-).
- **Breadth** (new): a root family whose members wake one another. In
  a passage holding "a draft from the window" and "she drew the
  outline", both surface as pulling. Pairs with write *scratch*: one
  hand-motion scratches, the other drags.

Done this session: optional `root` field (a shared id, e.g. `dragan`)
added to the `candidates.json` schema and to `build_lexicon.py`
OPTIONAL (validated as a non-empty string). First family queued, both
unverified and unscored: **draw** *drag* (picture sense) and **draft**
*a pulling*.

Other members noted for the family (from memory, unverified, not yet
queued):

- **drag** — the pull is still alive in the modern sense, so it has
  little buried. Probably a family member that anchors the others, not
  an entry of its own. Possibly via Old Norse *draga*; check.
- **dray** — a low cart without sides, dragged rather than rolled;
  Old English *dræge* "dragnet". Rare word, so a low frequency score.
- **drawer** — the box you pull out. Nobody hears the pull, though it
  is literal. A good candidate.
- **withdraw** — "draw back"; *with-* in its old sense "against, back".
  Two buried images in one word. A strong candidate.
- **drawing room** — short for *withdrawing room*. Belongs with
  withdraw rather than with the picture sense of draw; a trap to note.

Next step: a small prototype passage holding three or four family
members, to test whether siblings waking together lands before the
interface uses `root`. Open questions: does a sibling wake only when
the other is in the same passage, or always; how far a family reaches
(Old English root only, or back to PIE, where links grow hedged).

**Second family: \*peth₂- "to spread out" (PIE).** Came up while
weighing titles: *Mundus Patet* (the Roman pit of the dead, opened three
days a year) suggested *Verbum Patet*, "the word lies open". *Patet*
also means "it is evident", so the phrase holds both the thesis and the
illusion it undoes. *Verbum* and English *word* are cognates (PIE
\*werh₁- "to speak").

Queued, root id `peth2`, all unverified and unscored:

- **fathom** *span with outstretched arms* — Old English *fæþm* "the
  two arms outstretched, an embrace"; arm-span, then a depth measured
  in arm-spans, then to sound a depth, then to understand. "Can't
  fathom" hides the arms. The strongest of the three.
- **petal** *a thing spread flat* — Greek *petalon* "leaf", from
  *petalos* "spread out". The image may be thin.
- **patent** *open letter* — Latin *patentem* "lying open"; letters
  patent were royal grants issued unsealed. The noun hides the
  openness; the adjective keeps it.

**Hedged member: Latin *pandere* "to spread"** (expand, pace, pass,
compass). Perhaps from the same root. The link is debated (de Vaan,
*Etymological Dictionary of Latin*, is the usual reference; check the
exact entry before citing). *Pandere*'s own origin is not the question,
so this is not Contested Archaeology. What is disputed is its
membership in the family. Kept out of the `root` field, which asserts
shared descent; recorded as "perhaps" kin in fathom's editorial notes.
Open question: does a family need a hedged-membership marker, the way
contested entries carry "perhaps" theories? If so, it should follow the
same rules: sourced, always marked "perhaps", never shown as the only
reading.

**Third family: Proto-Germanic \*hag- "enclosure".** Root id `hag`.
Queued, unverified and unscored:

- **hedge** *fence with thornbush* — Old English *hecg*, a row of
  bushes planted as a fence. To hedge a bet was to fence in one's
  losses; to hedge a statement, to fence a claim with qualifiers.
  "She hedged" hides the thornbush. It also describes the lexicon's
  own method: a "perhaps" is a hedge planted around a claim. Adds to
  the thin Enclosures family (court, town, camera).
- **hawthorn** *hedge thorn* — Old English *haga* "enclosure" +
  *þorn*. Probably a family anchor rather than a strong entry.

Deeper, perhaps: PIE \*kagh- "to catch; wattle, fence" (Welsh *cae*,
perhaps *quay* via Gaulish). From memory and unsourced, so kept in
editorial notes only.

------------------------------------------------------------------------

## Start Here (as of 2026-09-26, end of session)

State: 288 verified entries (278 glossed, 10 contested) + 19 derived
forms = 307 words; ~40 recovered words per 1,000 in modern English.
`index.html` opens in the *Stir* view (text stirred in place: word →
root → image), with *Translate* as the second view; no estrangement
dial. `build_lexicon.py` validates before building. Everything pushed.

Last session (2026-09-26): homonym collection begun in `homonyms/`.
374-word Wiktionary shortlist, now under hand review; nothing added to
`canonical.json`. See the 2026-09-26 log entry above and
`homonyms/homonyms_handoff.md`. (2026-09-18: hedged glosses approved,
stir-fry built, two high-frequency passes 106 → 288, dial removed.)

Candidate next tasks (user to choose):

1. **Resume the stir-fry.** It was paused because too few words stirred
   (4–9 per 1,000); coverage is now ~40, so test whether new poems
   emerge on real prose. Ideas: "Stir all" ordered by `surprise_score`
   (strongest images first); saving or sharing poems beyond the
   clipboard; hover-stir feel (width jumps).
2. **Contested-words feature** — `theories` / `elsewhere` fields (policy
   decided: sourced, always "perhaps"). Six contested entries already
   carry sourced theories in `editorial_notes` (soul, silver, book,
   calm, human, religion); boy, girl, bride, sycophant still need
   research. Validator must require a `source` per theory. Plan
   `concept` ids in (see direction below).
3. **More coverage** — deeper down the `wordfreq` list (ranks
   1,500–6,000); revisit held words (place, island, fan, believe,
   doubt, satisfy, peculiar …, reasons in the logs).
4. **Homonyms.** Once the user has marked the shortlist, read the marks
   (review page linked in the 2026-09-26 log). Draft and verify both
   histories and their images for the keeps and maybes. Before any
   entry lands, the user decides: the `build_lexicon.py` change so one
   spelling can hold several entries; adding the Homonymous Archaeology
   clause; how the ghosts render (light direction picks one, or both
   tangled); whether polysemy renders differently; ratifying the Zipf
   3.0 cutoff.
5. **Constraint writing** (idea recorded 2026-09-29, see log). The
   writer composes a poem (e.g. 12 lines) in which every line holds one
   or more lexicon words, from the full lexicon or a random draw.

**Pending decision (user):** the zero-derivation verb gloss — a noun
gloss used as a verb where no verb image is attested (focused →
*hearthed*, checked → *kinged*). Written into `editorial.md` as
current practice; user has not confirmed it.

Direction: leaning toward parallel-language reading as where the
lexicon leads (not final; confirm after a prototype).

Smaller open items: old glosses that break in running text (capital,
cynic, desire as a noun, influence, possessives); singleton image
families; re-score `frequency_score` for the pre-2026-09-18 entries
(new ones use corpus counts).
