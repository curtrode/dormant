# dormant

**Semantic Archaeology** — a curated lexicon of forgotten images. Each entry
replaces a common English word with the literal meaning of its etymological
roots (window → *wind eye*, mortgage → *death pledge*), making ordinary prose
briefly strange without becoming unintelligible.

## The piece

`index.html` is the electronic-literature piece. Open it in a browser: paste
your own prose or pick a sample passage, and it renders a **translation** (roots
recovered) above your **original** text. Hover a recovered word to see the
source word and its etymon; the *estrangement* dial controls how many words are
recovered — at maximum, even the contested words surface, marked but never
glossed.

Runs from `file://` with no server — just open `index.html`.

## Files

- `index.html` — the electronic-literature piece
- `lexicon.js` — generated lexicon data (run `python3 build_lexicon.py` to rebuild from `canonical.json`)
- `build_lexicon.py` — bakes `canonical.json` into `lexicon.js`
- `canonical.json` — accepted, verified entries (production lexicon)
- `candidates.json` — research queue
- `editorial.md` — editorial policy, criteria, and methodology
- `poetics_of_semantic_archaeology.md` — conceptual essay
- `research_notes.md` — laboratory notebook
