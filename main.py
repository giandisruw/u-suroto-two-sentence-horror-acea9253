"""Two-Sentence Horror — make.fun entry.

The story (final, 244 characters):

    Every night my daughter tucks her doll in beside her and whispers
    goodnight to the man in the corner. Tonight the doll was already
    tucked in, and the whispering was coming from her bedroom — in her
    voice — while she stood beside me in the hall.

The scare: a nightly ritual the narrator has accepted as harmless —
a child whispering goodnight to "the man in the corner" — turns when
the ritual happens without the child. The doll is already tucked in,
and the whispering is still going, in the daughter's own voice, while
the real daughter stands beside the narrator. Whatever is in the room
has learned to sound like her, and it has been practising every night.

Revision note: the first draft was "Every night my daughter tucks
her doll in beside her and whispers goodnight to the man in the
corner. Tonight the doll was already tucked in when I checked on
her, and I heard whispering from her bedroom — in her voice — while
she stood beside me in the hall." (259 characters). It was flatter
in two places: "when I checked on her" was dead weight that only
explained how the narrator knew, and "I heard whispering" kept the
sound at arm's length. The revision cuts the whole "when I checked
on her" clause and changes "I heard whispering" to "the whispering
was coming from" — the definite article ties the sound back to the
nightly ritual of the first sentence, so the reader understands it
is the same whispering, now happening without the daughter. Fifteen
characters shorter, and the turn now lands on the reader instead of
being narrated to them.
"""

import argparse
import re
import sys
import tempfile
from pathlib import Path

# Final story (revised from the first draft; see docstring).
STORY = (
    "Every night my daughter tucks her doll in beside her and whispers "
    "goodnight to the man in the corner. Tonight the doll was already "
    "tucked in, and the whispering was coming from her bedroom \u2014 "
    "in her voice \u2014 while she stood beside me in the hall."
)

MAX_CHARS = 400


def count_sentences(text: str) -> int:
    """Count sentence-ending punctuation marks that end a sentence."""
    return len(re.findall(r"[.!?]+(?=\s|$)", text))


def validate(text: str) -> list[str]:
    """Return a list of validation failures (empty when valid)."""
    failures = []
    if not 1 <= len(text) <= MAX_CHARS:
        failures.append(
            f"length {len(text)} chars is outside 1-{MAX_CHARS}")
    if text != text.strip():
        failures.append("leading or trailing whitespace")
    if not text.strip():
        failures.append("only whitespace")
    if any(ord(ch) < 32 or ord(ch) == 127 for ch in text):
        failures.append("contains control characters")
    sentences = count_sentences(text)
    if sentences != 2:
        failures.append(f"has {sentences} sentences, expected exactly 2")
    return failures


def write_entry(path: Path) -> None:
    """Validate the story, then write exactly it (no trailing newline)."""
    failures = validate(STORY)
    if failures:
        raise SystemExit(f"invalid entry: {'; '.join(failures)}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(STORY.encode("utf-8"))


def self_test() -> int:
    """Validate, write twice to a temp dir, byte-compare, report, exit code."""
    checks = []

    failures = validate(STORY)
    checks.append(("1-400 chars, exactly 2 sentences, no stray "
                   "whitespace or control chars",
                   not failures, "; ".join(failures) or "ok"))

    with tempfile.TemporaryDirectory() as tmp:
        first = Path(tmp) / "first.txt"
        second = Path(tmp) / "second.txt"
        write_entry(first)
        write_entry(second)
        a = first.read_bytes()
        b = second.read_bytes()
        checks.append(("deterministic: two runs byte-identical",
                       a == b, f"{len(a)} bytes each" if a == b
                       else "outputs differ"))
        checks.append(("no trailing newline",
                       not a.endswith(b"\n"),
                       "ends with newline" if a.endswith(b"\n") else "ok"))
        checks.append(("decodes as UTF-8, exactly the story",
                       a.decode("utf-8") == STORY,
                       "round-trip ok"))
        checks.append(("exactly two sentences in the written file",
                       count_sentences(a.decode("utf-8")) == 2,
                       f"{count_sentences(a.decode('utf-8'))} sentences"))

    print(f"Entry: {STORY}")
    print(f"Characters: {len(STORY)} (limit {MAX_CHARS})")
    print(f"Sentences: {count_sentences(STORY)}")
    all_pass = True
    for name, passed, detail in checks:
        print(f"[{'PASS' if passed else 'FAIL'}] {name} — {detail}")
        all_pass = all_pass and passed
    print("SELF-TEST: " + ("PASS" if all_pass else "FAIL"))
    return 0 if all_pass else 1


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(
        description="Write the two-sentence horror story to entry.txt.")
    parser.add_argument(
        "output", nargs="?",
        default="/output/entry.txt",
        help="where to write the entry (default: /output/entry.txt)")
    parser.add_argument(
        "--self-test", action="store_true",
        help="validate, write twice to a temp dir, byte-compare, report")
    args = parser.parse_args(argv)
    if args.self_test:
        return self_test()
    write_entry(Path(args.output))
    return 0


if __name__ == "__main__":
    sys.exit(main())
