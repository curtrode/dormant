# Dormant (from *dormire*, to sleep) — Design

A browser-based e-lit piece by Curt Rode. The reader pastes a text of their choosing into a field. The piece "translates" it by swapping words for the literal glosses of their etymons — *mortgage* becomes *death pledge*, *window* becomes *wind eye*, *muscle* becomes *little mouse*. Hovering (or tapping) a substituted word reveals the original beneath it. The etymologies are not dead; they are asleep in the words, and the reader's attention wakes them.

This is **v0**, and v0 is deliberately a *coverage test*: the piece's central risk is not the mechanism (which is simple) but the lexicon — whether enough English words carry glosses vivid enough that an arbitrary pasted text transforms into something interesting rather than mostly passing through untouched. Every scoping decision below serves answering that question quickly.

---

## 1. Decisions log

Settled forks, with reasoning. Do not re-litigate these during the build.

1. **Calque mode first.** Two substitution modes were identified: (a) ancestral-form substitution (mortgage → *mort gage* → Latin roots), buildable from structured etymology databases; (b) calque substitution (mortgage → "death pledge"), which requires glosses that live in etymology prose, not structured fields. Mode (b) is the piece the author's founding example implies and the poetically stronger mode — and it is the risky one, so it goes first. Mode (a) shares nearly all infrastructure and becomes a second lexicon dropped into working machinery later.
2. **Hover-reveal rendering.** The translated text stands in place; the original is recoverable on hover (desktop) / tap (touch). Consequence: substitutions can afford to be strange in context, because the reader can always recover the original — this loosens the semantic-legibility bar on the lexicon.
3. **Hybrid lexicon pipeline.** LLM-generated candidate lexicon (~300–400 entries), cross-checked against a second model from a different provider (independent fabrications rarely agree, so disagreement flags entries for review — but agreement is not proof; both models share training corpora and can share folk etymologies), then verified against Wiktionary as ground truth. False etymologies are costlier here than sparse coverage: the piece implicitly claims philological authority, and hover invites inspection of every substitution.
4. **Static JSON lexicon, browser-only.** No runtime LLM, no API dependency. The lexicon ships as a static file; the app is fully client-side.
5. **Title.** *Dormant (from dormire, to sleep)* — the parenthetical is a hover-reveal flattened into typography, teaching the reader the piece's gesture before they touch anything. Repo name: `dormant`. The full title is the print/citation form.

---

## 2. The reading experience

1. The reader arrives at a near-empty page: the title, a paste field, minimal instruction (wording TBD — see §8).
2. The reader pastes or types a text and submits (or the piece translates live on input — builder may propose either; default: translate on submit for v0 simplicity).
3. The text re-renders with substitutions in place. Substituted words are *subtly* distinguishable — enough that the reader can find them, not so much that the page reads as a diff. (Exact treatment is an open question, §8; use a faint underline or slight weight shift as the working default.)
4. Hovering a substituted word reveals the original. On touch devices, tap serves the same role. The presentation of the reveal (in-place momentary swap-back, tooltip above, layered ghost) is an open question (§8); default for v0: **in-place swap-back** while hover/press is held — it is the simplest and keeps the reveal inside the text rather than in chrome.
5. Unsubstituted words pass through unchanged, with no special treatment in v0.

---

## 3. Substitution model

Pure logic, no DOM coupling.

- **Tokenization.** Split input into word and non-word tokens, preserving all whitespace and punctuation exactly. Substitution never touches non-word tokens.
- **Matching.** Case-insensitive lookup against the lexicon. v0 handles two cheap inflection cases only: naive plural stripping (*mortgages* → *mortgage*, re-pluralize the gloss head-word naively: *death pledges*) and case restoration (sentence-initial capitalization carries onto the gloss's first word). Full lemmatization (compromise.js) is deferred (§7) — bring it in only if the coverage test shows inflection is a meaningful leak.
- **Multi-word glosses.** Many glosses are two words (*death pledge*, *wind eye*). The substituted span is one interactive unit — hover anywhere in "death pledge" reveals "mortgage." Layout simply reflows; no attempt to preserve line geometry in v0.
- **Collisions.** If a gloss itself contains a lexicon word (e.g., a gloss containing *day*), do **not** recursively substitute. One pass, source words only.

---

## 4. Lexicon

### 4.1 Format

`data/lexicon.json`, an object keyed by lowercase source word:

```json
{
  "mortgage": {
    "gloss": "death pledge",
    "etymon": "mort gage",
    "language": "Old French",
    "note": "mort 'dead' + gage 'pledge'; so called because the deal dies on payment or forfeit",
    "verified": true
  }
}
```

- `gloss` — the literal rendering used for substitution. Lowercase; case restored at render.
- `etymon`, `language`, `note` — provenance, displayed nowhere in v0 but kept for a future "inspect" affordance and for verification bookkeeping.
- `verified` — true only after the Wiktionary check (§4.2). The app loads unverified entries in dev, but a production build should warn on any `verified: false`.

### 4.2 Pipeline (parallel track, not app code)

This work happens between the author and LLM chat sessions, not in Claude Code, but the builder should know the shape:

- **L1 — Generation.** An LLM produces candidate entries from a frequency-ranked English wordlist, biased toward words with vivid literal glosses.
- **L2 — Cross-check.** A second model from a different provider reviews the candidate list; disagreements are flagged for human review.
- **L3 — Verification.** Each surviving entry is checked against Wiktionary (its REST API is free and CORS-friendly; a small script in `tools/` may assist). Only then is `verified` set true.

A hand-picked **seed lexicon** of ~20 unimpeachable entries (mortgage, window, muscle, companion, daisy, disaster, sarcophagus, etc.) ships first so Milestones 1–2 never wait on the pipeline.

### 4.3 The coverage question

Milestone 3 ends with an explicit evaluation: paste several real texts of different registers (a news paragraph, a poem, casual prose, legalese) and assess substitution density and texture. This is the v0 verdict. Possible outcomes: the concept works at this lexicon size; it needs a larger lexicon (scale L1–L3); or density is structurally too thin and the design needs rethinking (e.g., loosening what counts as a gloss). That judgment belongs to the author.

---

## 5. Milestones

Each milestone ends with the author looking at the running piece. Do not start the next milestone unprompted.

- **M1 — Scaffold + substitution.** Vite + TypeScript scaffold; paste field; tokenizer; substitution pass against the seed lexicon; translated text renders (no reveal yet). Author sees "death pledge" appear in a pasted sentence.
- **M2 — Reveal.** Hover swap-back on desktop; tap/press equivalent on touch; subtle marking of substituted spans. Author reads a translated text and wakes words.
- **M3 — Full lexicon + coverage evaluation.** Integrate the pipeline-produced lexicon; plural/case handling exercised at scale; the §4.3 evaluation session.

---

## 6. Technical requirements

- Vite + TypeScript. **Plain DOM rendering** — no Three.js, no canvas, no shaders in v0. Type is the material; HTML text is the right substrate.
- No frameworks, no React, no state libraries. Dependencies for v0: `vite`, `typescript` only. `compromise` may be added later by explicit decision (§7).
- Substitution model is pure and renderer-agnostic (`src/substitute/` has no DOM imports).
- Works from a static host (Vercel); no server component.

---

## 7. Deferred (explicitly out of v0)

- **Mode (a): ancestral-form substitution** — second lexicon (etymwn / kaikki-derived), same pipeline; possibly a reader-facing mode toggle or depth slider (surface gloss → older forms).
- **Full lemmatization** via compromise.js, if the coverage test shows inflection leakage matters.
- **Runtime LLM translation** for words outside the lexicon — the long-term horizon the author named at the start; v0's static lexicon is the trustworthy floor beneath it.
- **Inspect affordance** — exposing `etymon` / `language` / `note` on a longer press or click.
- **Visible-history modes** — strikethrough, layering, any diff-like rendering (rejected for v0 in favor of hover, but not forever).
- **Typographic treatment of dormancy** — e.g., substituted words rendered slightly "asleep" (reduced weight?) and waking on hover. Attractive; defer until the mechanism is judged.
- **Sharing/export** of translated texts.

---

## 8. Open questions (for the author, not the builder)

Do not resolve these; where a default is given, use it and say so.

1. Title rendering on the page: bare **Dormant** with the gloss itself revealed on hover (interaction as the native form), or the full parenthetical displayed. *Default: bare title with hover-gloss — it demonstrates the mechanism.*
2. Visual marking of substituted spans: none, faint underline, weight shift, color. *Default: faint dotted underline.*
3. Reveal presentation: in-place swap-back vs tooltip vs ghost layer. *Default: in-place swap-back.*
4. Translate on submit vs live on input. *Default: on submit.*
5. Instruction wording on the landing state, if any.
6. Typeface.
7. What happens to the pasted original — discarded, or recoverable whole (an "unsleep" control)? *Default: no control; the hover is the only recovery.*
