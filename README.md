# Mundus patet, verbum patet

*The world lies open, the word lies open* — notes towards a Semantic
Archaeology. (Repository name: `dormant`.)

A curated lexicon of forgotten images. Each entry
replaces a common English word with the literal meaning of its etymological
roots (window → *wind eye*, mortgage → *death pledge*), making ordinary prose
briefly strange without becoming unintelligible.

297 verified entries as of 2026-10-02 (plus 19 derived forms such as
government, president and company), spanning Old English/Norse household
and kinship terms, Latin/Greek abstractions, law & religion, medicine,
trade & textiles, and measurement. Two high-frequency passes — one on
19th-century novels (world → *age of man*, answer → *counter-oath*), one
on modern English (video → *I-see*, worry → *strangle*, phone → *far
voice*) — raised coverage of modern prose to about 40 recovered words
per 1,000. See `research_notes.md` for the session
log and open research domains.

## The piece

The piece has two modes, side by side under the title: **Read** and
**Write**. The title is from the Roman *mundus patet*, "the world is
open", the three days a year the pit of the dead was uncovered; a
footer note on both pages explains it.

**Read** (`docs/index.html`). Open it in a browser: paste
your own prose or pick a sample passage, and it renders a **translation** (roots
recovered) above your **original** text. Hover a recovered word to see the
source word and its etymon. Contested words are marked but never
glossed. In the default *Stir* view the text starts as plain
English and changes in place as the mouse passes over it — each word sinks
to its root and surfaces as its image (*window* → *vindauga* → *wind eye*),
so the reader stirs a new poem out of the prose. Three sample passages are built in: *The household*, *The scholar* and
*The sentence*.

**Write** (`docs/write.html`, prototype). The writer composes a poem in
which every line holds a lexicon word: from a dealt hand, or from the
whole lexicon, which is listed by image family with a find box. When
every line holds, the poem *bleeds* (images rise as ghosts over the
words) or *stirs*.

Research continues in three directions: homonyms (one spelling, unrelated
words: `homonyms/`), root families (entries that share a root wake together;
the optional `root` field), and hedged theories for contested words
(sourced, always marked "perhaps"). See **Start Here** at the end of
`research_notes.md`.

Runs from `file://` with no server — just open `docs/index.html`. The same
folder is what GitHub Pages publishes (Settings → Pages → main / docs), so the
piece is also live on the web; nothing else in the repository is served.

## Files

- `docs/index.html` — Read mode, the electronic-literature piece, and what Pages serves
- `docs/write.html` — Write mode, constraint writing (prototype): a poem in which every line must hold a word from a dealt hand or the whole lexicon; finished, it bleeds (images rise as ghosts over the words) or stirs
- `docs/stir.js` — matching and stirring engine shared by both pages
- `docs/lexicon.js` — generated lexicon data (run `python3 build_lexicon.py` from the repository root to rebuild from `canonical.json`)
- `build_lexicon.py` — validates `canonical.json` (required fields, score ranges,
  contested entries unglossed, unique words, sources on every entry and form),
  then bakes it into `docs/lexicon.js`; `--check` validates only
- `canonical.json` — accepted, verified entries (production lexicon)
- `candidates.json` — research queue (verified candidates carry scores and a verdict in `editorial_notes`)
- `editorial.md` — editorial policy, criteria, and methodology
- `poetics_of_semantic_archaeology.md` — conceptual essay
- `research_notes.md` — laboratory notebook
- `homonyms/` — homonym collection: Wiktionary finder and filter scripts, the 374-word shortlist, the handoff notes
