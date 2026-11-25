"""Worst AI advice, variant 5: confident how-to help that turns
catastrophic in its closing words.

The entry is one tidy AI-voice instruction: dry a wet phone by
microwaving it for 30 seconds. The badness is specific enough to
follow, funny on first read, and regrettable the moment it is acted
on. The reassurance in the second half, that the heat "removes the
water safely", is the punchline, delivered without any explanation
or second line.

How the entry is aimed at the judge's criteria:
1. Worstness: the advice destroys the very thing it claims to save.
2. Funniness: the joke lands immediately, carried by the calm,
   helpful tone rather than by exaggeration.
3. Tightness: a single line, a single incident, no wasted words.
4. AI voice: a confident how-to answer, the kind of tidy reply a
   helpful assistant gives to an everyday tech problem.
5. Concreteness: a real situation (a wet phone) and a real action
   (30 seconds in the microwave), so the badness is vivid.
6. Originality: a fresh topic and a fresh "To X, do Y; the Z"
   shape versus variants 1 to 4 (production database, passwords,
   boiling water for a sore throat, a match to find a gas leak).
"""

from pathlib import Path

# The entry: one confident, tidy AI-voice instruction to do something
# concretely catastrophic. No explanation, no second line. Fresh
# topic versus variants 1-4: a wet phone in the microwave.
ENTRY = (
    "To dry a wet phone, microwave it for 30 seconds; "
    "the heat removes the water safely."
)

OUTPUT_PATH = Path("/output/entry.txt")

MAX_LENGTH = 140
MIN_LENGTH = 1


def _normalize(text: str) -> str:
    """Strip surrounding whitespace; the gate counts what remains."""
    return text.strip()


def _check_not_empty(text: str) -> None:
    if not text:
        raise ValueError("entry must not be only whitespace")


def _check_length(text: str) -> None:
    if not MIN_LENGTH <= len(text) <= MAX_LENGTH:
        raise ValueError(
            f"entry must be {MIN_LENGTH}-{MAX_LENGTH} characters, "
            f"got {len(text)}"
        )


def _check_single_line(text: str) -> None:
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")


def _validate(text: str) -> str:
    """Run the whole gate on the normalized text and return it."""
    checked = _normalize(text)
    _check_not_empty(checked)
    _check_length(checked)
    _check_single_line(checked)
    return checked


def _write(text: str) -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    # Write exactly the one line, no trailing newline: the gate counts
    # every character, and the tie-break favours the smaller text.
    OUTPUT_PATH.write_text(text, encoding="utf-8")


def _verify(text: str) -> None:
    """Confirm what landed on disk is exactly the checked text."""
    written = OUTPUT_PATH.read_text(encoding="utf-8")
    if written != text:
        raise ValueError("written entry does not match the checked text")


def build_entry() -> str:
    """Return the validated entry text, ready to be written."""
    return _validate(ENTRY)


def main() -> None:
    text = build_entry()
    _write(text)
    _verify(text)


if __name__ == "__main__":
    main()
