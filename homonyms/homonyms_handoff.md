# Dormant — Homonym Collection: Handoff

Context carried over from a chat session (2026-09-26). Nothing in the Dormant repo has been changed.

## Working rules
- Consult Curt before any code or repo change.
- The homonym collection is **standalone** until Curt decides to fold anything into `canonical.json`.

## Decisions so far
- **Creative over corrective.** Homonyms are places where ghosts overlap, not a disambiguation problem.
- **Generous threshold.** One vivid buried image plus one plain history qualifies.
- **Declared exception.** Homonyms get their own clause in `editorial.md`, modeled on Contested Archaeology (draft below, not yet added).

## Still open
- Rendering under raking light: angle-dependent (light direction chooses the ghost) vs. tangled simultaneity (both surface, interlocked).
- Whether polysemy (*pupil*: one sign repainted) renders differently from true homonymy (*mint*: two signs).
- Whether contested origins get a fragmentary-letters treatment.
- Frequency floor (Zipf 3.0) and Wiktionary-derived source were Claude's choices, not yet ratified.

## Known conflict
`build_lexicon.py` rejects duplicate words (the page looks entries up by spelling), so one spelling cannot currently hold two entries. Resolving this is a code change awaiting Curt's go-ahead.

## Data
- `dormant_homonym_candidates.csv` — 1,560 candidates; columns: `tier`, `word`, `zipf`, `split_in`, `distinct_etyma`, `in_dormant` (72 already in the lexicon).
- `find_homonym_candidates.py` — the generating script.
- `dormant_homonym_shortlist.csv` — 374 words that Wiktionary splits into two or more separate histories; columns: `word`, `zipf`, `in_dormant`, `wiktionary_etymologies`, `histories`, then `sense_N` / `origin_N` for up to four histories.
- `filter_homonym_candidates.py` — cuts the candidates to the shortlist (method in its docstring).

**Regenerating.** Needs `pandas`, `pyarrow`, `wordfreq`. Download `etymology.parquet` from the droher/etymology-db 2023-12 release, filter it to English (`pd.read_parquet('etymology.parquet', filters=[('lang','==','English')]).to_parquet('en.parquet')`), then run the script from the directory holding `en.parquet`. It reads `../canonical.json` and writes the CSV next to itself. The data is ~140 MB, so keep it out of the repo.

**Method.** Source: droher/etymology-db (Wiktionary-derived, 2023-12 release), which merges each word's etymology sections into one record. The script flags words whose ancestry contains dissimilar deep etyma within one family (Latin, Greek, Proto-Germanic, PIE, Old Norse, Arabic, etc.), or an Old English line beside an unrelated French one. Filtered to wordfreq Zipf ≥ 3.0 and lowercase alphabetic words.

**Quality.** Recall is good: bank, mint, grave, school, sound, date, host, quarry, policy, fair, temple, bark all found; kind and salary correctly skipped; **cleave missed**. Precision is poor (likely a third or less): verb/participle pairs (*data*/*datus*) and compound roots read as separate lineages, and related forms inflate counts (quarry shows five Latin roots for two histories). The A/B tier is a weak signal, not a quality ranking.

**Shortlist (2026-09-26).** `filter_homonym_candidates.py` fetches each candidate's Wiktionary page and keeps words with two or more numbered etymology sections that hold current senses and descend from different roots. 1,560 → 374. All twelve known homonyms above survive, plus *fan* and *guy*; *pupil*, *minute*, *kind* and *salary* drop out as one root each. Remaining noise, for the hand cull: function words and names with an unrelated loan or proper noun (*on* / Japanese *on*, *son* / Cuban *son*, *ben*, *sam*), clippings of compounds on the word itself (*mother*, *media*), and Wiktionary noun/verb splits the stem match misses (*house*). Regenerate from the `homonyms/` folder with `python3 filter_homonym_candidates.py <cache.json>`; the first run fetches about 1,560 pages at 50 per request and takes a few minutes. Next step: Claude drafts both histories and images for the survivors, and Curt marks keep / reject.

## Draft clause for editorial.md (not yet added)

**Homonymous Archaeology**

Some common English words are two words wearing one spelling: separate histories that converged on the same surface by coincidence (mint → *Juno's warning-temple* / *the herb*; grave → *dug pit* / *heavy*). Rather than choosing one history, maintain a distinct **Homonymous Archaeology** category that presents both.

This category deliberately contradicts the lexicon's other rules:

- **Threshold is generous.** A homonym qualifies if at least one of its histories yields a vivid image. The other may be plain.
- **One spelling, several entries.** Each history is a separate entry sharing a word, each with its own etymon, gloss, and verification source.
- **Only true homonymy.** Senses that grew from one root (*pupil*, "little doll": student and eye) are polysemy and are admitted, if at all, as a single entry.

Every history still requires independent verification. The generosity applies to the image, never to the evidence.

Where most entries recover a forgotten image, homonymous entries reveal that a surface can hold unrelated pasts, making coincidence itself part of the literary experience.
