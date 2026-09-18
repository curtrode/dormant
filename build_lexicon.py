#!/usr/bin/env python3
"""Bake canonical.json into lexicon.js so index.html runs from file:// with no server.

The lexicon is a curated literary corpus; canonical.json remains the single
source of truth. Re-run this whenever canonical.json changes:

    python3 build_lexicon.py           # validate, then write lexicon.js
    python3 build_lexicon.py --check   # validate only

The build refuses to write lexicon.js if canonical.json fails validation.
"""
import json
import sys

FIELDS = ("word", "gloss", "etymon", "language", "note", "part_of_speech",
          "recovery_type", "image_family", "surprise_score")

REQUIRED = ("word", "gloss", "etymon", "language", "note", "part_of_speech",
            "image_family", "recovery_type", "surprise_score", "frequency_score",
            "confidence_score", "verified", "verification_source", "editorial_notes")
OPTIONAL = ("forms", "plural", "verb_gloss")
RECOVERY_TYPES = ("literal", "conceptual", "semantic", "contested")
PARTS_OF_SPEECH = ("noun", "verb", "adjective", "adverb")

FORM_REQUIRED = ("word", "gloss", "part_of_speech", "verification_source")
FORM_OPTIONAL = ("plural", "surprise_score")


def is_score(v):
    return isinstance(v, int) and not isinstance(v, bool) and 1 <= v <= 5


def is_text(v):
    return isinstance(v, str) and v.strip() != ""


def validate(data):
    """Return a list of human-readable problems; empty means canonical.json is sound."""
    errors, seen = [], {}

    def claim(word, where):
        # Words must be unique across entries and forms: the page looks them up by word.
        key = word.lower() if isinstance(word, str) else word
        if key in seen:
            errors.append(f"{where}: duplicate word (also {seen[key]})")
        else:
            seen[key] = where

    for i, e in enumerate(data.get("entries", [])):
        where = f"entry {i} ({e.get('word', '?')})"
        missing = [k for k in REQUIRED if k not in e]
        unknown = [k for k in e if k not in REQUIRED + OPTIONAL]
        if missing:
            errors.append(f"{where}: missing {', '.join(missing)}")
        if unknown:
            errors.append(f"{where}: unknown field(s) {', '.join(unknown)} (typo?)")
        if not is_text(e.get("word")):
            errors.append(f"{where}: word must be a non-empty string")
            continue
        claim(e["word"], where)

        rt = e.get("recovery_type")
        if rt not in RECOVERY_TYPES:
            errors.append(f"{where}: recovery_type {rt!r} not in {RECOVERY_TYPES}")
        if rt == "contested":
            # Contested entries never receive an invented image.
            if e.get("gloss") is not None:
                errors.append(f"{where}: contested entry must have gloss null")
            if e.get("surprise_score") is not None:
                errors.append(f"{where}: contested entry must have surprise_score null")
            if e.get("forms"):
                errors.append(f"{where}: contested entry cannot have forms")
            if "plural" in e or "verb_gloss" in e:
                errors.append(f"{where}: contested entry cannot have plural or verb_gloss")
        else:
            if not is_text(e.get("gloss")):
                errors.append(f"{where}: gloss must be a non-empty string")
            if not is_score(e.get("surprise_score")):
                errors.append(f"{where}: surprise_score must be an integer 1-5")

        if e.get("part_of_speech") not in PARTS_OF_SPEECH:
            errors.append(f"{where}: part_of_speech {e.get('part_of_speech')!r} not in {PARTS_OF_SPEECH}")
        if "plural" in e and (e.get("part_of_speech") != "noun" or not is_text(e["plural"])):
            errors.append(f"{where}: plural must be a non-empty string on a noun")
        # verb_gloss: a noun entry's gloss when the word is used as a verb
        # (answer -> "counter-oath", but answered -> "swore against").
        if "verb_gloss" in e and (e.get("part_of_speech") == "verb" or not is_text(e["verb_gloss"])):
            errors.append(f"{where}: verb_gloss must be a non-empty string on a non-verb entry")
        for k in ("frequency_score", "confidence_score"):
            if not is_score(e.get(k)):
                errors.append(f"{where}: {k} must be an integer 1-5")
        if e.get("verified") is not True:
            errors.append(f"{where}: canonical entries must be verified (move to candidates.json?)")
        if not is_text(e.get("verification_source")):
            errors.append(f"{where}: verification_source is required")

        forms = e.get("forms", [])
        if not isinstance(forms, list):
            errors.append(f"{where}: forms must be a list")
            continue
        for j, f in enumerate(forms):
            fwhere = f"{where} form {j} ({f.get('word', '?')})"
            missing = [k for k in FORM_REQUIRED if not is_text(f.get(k))]
            unknown = [k for k in f if k not in FORM_REQUIRED + FORM_OPTIONAL]
            if missing:
                errors.append(f"{fwhere}: missing or empty {', '.join(missing)}")
            if unknown:
                errors.append(f"{fwhere}: unknown field(s) {', '.join(unknown)} (typo?)")
            if is_text(f.get("word")):
                claim(f["word"], fwhere)
            if f.get("part_of_speech") not in PARTS_OF_SPEECH:
                errors.append(f"{fwhere}: part_of_speech {f.get('part_of_speech')!r} not in {PARTS_OF_SPEECH}")
            if "surprise_score" in f and not is_score(f["surprise_score"]):
                errors.append(f"{fwhere}: surprise_score must be an integer 1-5")
            if "plural" in f and (f.get("part_of_speech") != "noun" or not is_text(f["plural"])):
                errors.append(f"{fwhere}: plural must be a non-empty string on a noun form")
    return errors


def build(data):
    entries = []
    for e in data["entries"]:
        entry = {k: e.get(k) for k in FIELDS}
        for k in ("plural", "verb_gloss"):            # entry-only: forms never inherit these
            if e.get(k):
                entry[k] = e[k]
        entries.append(entry)
        # Derived forms (governor -> government) inherit the parent's etymon,
        # note, and family; they carry their own word, gloss, and part of speech.
        for f in e.get("forms", []):
            form = {k: f.get(k, e.get(k)) for k in FIELDS}
            form["base"] = e["word"]
            if f.get("plural"):
                form["plural"] = f["plural"]
            entries.append(form)
    entries.sort(key=lambda e: e["word"])
    payload = json.dumps(entries, ensure_ascii=False, indent=2)
    banner = ("// GENERATED by build_lexicon.py from canonical.json — do not edit by hand.\n"
              "// Re-run `python3 build_lexicon.py` after changing canonical.json.\n")
    with open("lexicon.js", "w", encoding="utf-8") as f:
        f.write(banner)
        f.write("window.LEXICON = " + payload + ";\n")
    return len(entries)


def main():
    data = json.load(open("canonical.json", encoding="utf-8"))
    errors = validate(data)
    if errors:
        print(f"canonical.json failed validation ({len(errors)} problem(s)); lexicon.js not written:",
              file=sys.stderr)
        for err in errors:
            print("  - " + err, file=sys.stderr)
        sys.exit(1)
    if "--check" in sys.argv[1:]:
        print(f"canonical.json OK ({len(data['entries'])} entries).")
        return
    print(f"Wrote lexicon.js with {build(data)} entries.")


if __name__ == "__main__":
    main()
