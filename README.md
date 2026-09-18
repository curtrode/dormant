# dormant

**Semantic Archaeology** — a curated lexicon of forgotten images. Each entry
replaces a common English word with the literal meaning of its etymological
roots (window → *wind eye*, mortgage → *death pledge*), making ordinary prose
briefly strange without becoming unintelligible.

193 verified entries as of 2026-09-18 (plus 19 derived forms such as
government, president and company), spanning Old English/Norse household
and kinship terms, Latin/Greek abstractions, law & religion, medicine,
trade & textiles, and measurement. A high-frequency pass (world → *age of
man*, friend → *loving one*, answer → *counter-oath*) raised coverage of
ordinary prose to about 25 recovered words per 1,000. See `research_notes.md` for the session
log and open research domains.

## The piece

`index.html` is the electronic-literature piece. Open it in a browser: paste
your own prose or pick a sample passage, and it renders a **translation** (roots
recovered) above your **original** text. Hover a recovered word to see the
source word and its etymon; the *estrangement* dial controls how many words are
recovered — at maximum, even the contested words surface, marked but never
glossed. In the default *Stir* view the text starts as plain
English and changes in place as the mouse passes over it — each word sinks
to its root and surfaces as its image (*window* → *vindauga* → *wind eye*),
so the reader stirs a new poem out of the prose. Three sample passages are built in: *The household*, *The scholar* and
*The sentence*.

Coverage of ordinary prose is still thin; the next research pass targets
high-frequency words. Directions under consideration: a *stir-fry* interface
(after Jim Andrews) for stirring pasted text word by word, parallel-language
reading, and hedged theories for contested words (now approved: sourced
theories, always marked "perhaps"). See **Start Here** at the end
of `research_notes.md`.

Runs from `file://` with no server — just open `index.html`.

## Files

- `index.html` — the electronic-literature piece
- `lexicon.js` — generated lexicon data (run `python3 build_lexicon.py` to rebuild from `canonical.json`)
- `build_lexicon.py` — validates `canonical.json` (required fields, score ranges,
  contested entries unglossed, unique words, sources on every entry and form),
  then bakes it into `lexicon.js`; `--check` validates only
- `canonical.json` — accepted, verified entries (production lexicon)
- `candidates.json` — research queue
- `editorial.md` — editorial policy, criteria, and methodology
- `poetics_of_semantic_archaeology.md` — conceptual essay
- `research_notes.md` — laboratory notebook
