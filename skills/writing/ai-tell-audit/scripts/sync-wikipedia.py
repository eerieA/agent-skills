#!/usr/bin/env python3
"""Refresh the auto-generated tell blocks in craft/patterns.md from Wikipedia.

Source: Wikipedia "Signs of AI writing" (WikiProject AI Cleanup). That page
maintains lists of AI-tell vocabulary and phrases. This script pulls them and
rewrites ONLY the marked blocks in patterns.md:

    <!-- SYNC:<NAME>:START -->
    ...auto-generated...
    <!-- SYNC:<NAME>:END -->

Three blocks are maintained (one page fetch, looped over a config table):
    VOCAB   — overused single words (A3)
    PUFFERY — puffery / promotional phrases (A1, A2)
    COMMS   — chatbot / prompt-refusal correspondence phrases (C3)

Everything else in patterns.md — hand-written patterns, examples, tiers — is
left untouched. Structure patterns are NOT synced: they are concepts described
in prose, not extractable lists, and their explanations do not drift with model
releases, so they stay hand-curated.

The skill works fully without ever running this; it exists so the phrase lists
do not silently drift as the community guide evolves.

Usage:
    python sync-wikipedia.py              # rewrite every block in place
    python sync-wikipedia.py --check      # exit 1 if any block is stale (a nudge)
    python sync-wikipedia.py --dry-run    # print new blocks, write nothing
    python sync-wikipedia.py --only COMMS # restrict to one block (repeatable)

Deliberately dependency-free (urllib + stdlib) and deliberately narrow: one
source, a fixed set of blocks. Keep it that way — the point is to avoid the
multi-module sync sprawl that makes a skill clunky. Each block UNIONS its scrape
with a curated baseline (so a bad parse can never shrink a list), and a human
reviews the --check diff before syncing.
"""
from __future__ import annotations

import argparse
import html
import re
import sys
import urllib.request
from pathlib import Path

WIKI_URL = (
    "https://en.wikipedia.org/w/index.php"
    "?title=Wikipedia:Signs_of_AI_writing&action=raw"
)
PATTERNS = Path(__file__).resolve().parent.parent / "craft" / "patterns.md"

# Tokens that show up italicized near these sections but are prose, not tells.
STOPWORDS = {
    "the", "and", "for", "that", "with", "this", "from", "wikipedia",
    "article", "articles", "text", "writing", "words", "word", "see", "also",
    "not", "examples", "example", "empirical", "causal", "correlate",
    "empirically", "such", "these", "those", "more", "most", "often",
    # wiki-chrome that leaks in near the citation / help apparatus
    "access-date", "on wikipedia", "more detailed breakdown",
}

# ── Block config ────────────────────────────────────────────────────────
# One entry per marked block. `mode` decides extraction shape:
#   "word"   — single tokens only (spaces rejected); the overused-vocab case
#   "phrase" — multi-word phrases allowed (2..6 words); puffery / comms
# `hints` are lowercased substrings to locate the section in the raw wikitext.
# `baseline` is the curated floor; the scrape only ever ADDS to it.
# `rejected` is the curated deny-list: scraped candidates a human reviewed and
#   chose NOT to keep (too broad, wrong block, duplicate). Subtracted from every
#   result so --check stops re-flagging them as "new" on each run. Add a word
#   here when you reject it; the block config is the memory of that decision.
BLOCKS = [
    {
        "marker": "VOCAB",
        "mode": "word",
        "hints": ("word choice", "vocabulary", "overused", "specific words"),
        "baseline": {
            "actually", "additionally", "align", "boasts", "bolstered", "crucial",
            "delve", "emphasize", "emphasizing", "enduring", "enhance", "foster",
            "fostering", "garner", "highlight", "highlighting", "interplay",
            "intricate", "key", "landscape", "pivotal", "showcase", "showcasing",
            "tapestry", "testament", "underscore", "valuable", "vibrant",
        },
        "rejected": set(),
    },
    {
        "marker": "PUFFERY",
        "mode": "phrase",
        "hints": ("puffery", "promotional", "exaggerat", "editorializ"),
        "baseline": {
            "boasts", "breathtaking", "commitment to", "contributing to the",
            "cutting-edge", "deeply rooted", "enduring legacy", "evolving landscape",
            "exemplifies", "focal point", "groundbreaking", "in the heart of",
            "indelible mark", "is a testament", "key turning point", "must-visit",
            "nestled", "plays a vital role", "profound", "reflects broader",
            "renowned", "rich tapestry", "seamless", "setting the stage for",
            "stands as", "state-of-the-art", "stunning", "transformative",
            "underscores its importance", "unparalleled",
        },
        # Reviewed and dropped: duplicates of VOCAB (-ing verbs, single words) or
        # too broad/context-dependent to flag as puffery on their own.
        "rejected": {
            "boasts a", "diverse array", "enhancing", "featuring", "may vary",
            "natural beauty", "rich", "showcasing", "vibrant", "worth noting",
        },
    },
    {
        "marker": "COMMS",
        "mode": "phrase",
        "hints": ("communication", "chatbot", "prompt refusal", "i hope this",
                  "collaborative"),
        "baseline": {
            "as an ai language model", "as a large language model", "certainly",
            "great question", "here is a", "i cannot provide",
            "i hope this email finds you well", "i hope this helps",
            "is there anything else", "let me know", "let me know if", "of course",
            "would you like me to", "you're absolutely right",
        },
        "rejected": set(),
    },
]


def fetch(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "ai-tell-audit-sync/1.0"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read().decode("utf-8", "replace")


def _clean(token: str) -> str:
    return html.unescape(token).strip().strip(".,;:").lower()


def _looks_like_example_prose(raw: str) -> bool:
    """Reject scraped runs that are illustrative sentences, not tell phrases.

    The guide quotes real article snippets to demonstrate a tell (e.g.
    "''Bakunutan'' was hispanized to ''Bacnotan''"). Those leak in as long,
    proper-noun-heavy, verb-tensed runs. Tell phrases are short, lowercase,
    and don't read as a full clause about a specific subject.
    """
    if "'" in raw or '"' in raw:          # residual markup from merged runs
        return True
    if re.search(r"\b(was|were|is hispanized|ventured|refers to|began)\b", raw):
        return True
    if re.search(r"[A-Z]", raw) and len(raw.split()) > 2:  # proper-noun sentence
        return True
    return False


def extract(wikitext: str, hints: tuple[str, ...], mode: str) -> set[str]:
    """Pull candidate words/phrases from the section(s) matching `hints`.

    We scan italic/bold markup runs (''x'' / '''x'''), which is how the guide
    marks example words and phrases. Heuristic by design — the union with the
    baseline and the human review step are what make it safe. A tighter window
    (1800 chars) keeps one section's hint from bleeding into the next.
    """
    lower = wikitext.lower()
    found: set[str] = set()
    for hint in hints:
        idx = lower.find(hint)
        if idx == -1:
            continue
        window = wikitext[idx: idx + 1800]
        for m in re.finditer(r"'{2,3}([A-Za-z][A-Za-z '\-]{1,40})'{2,3}", window):
            token = m.group(1)
            if mode == "word":
                for part in re.split(r"[,/]| or | and ", _clean(token)):
                    part = _clean(part)
                    if 2 < len(part) <= 20 and " " not in part and part not in STOPWORDS:
                        found.add(part)
            else:  # phrase
                if _looks_like_example_prose(token):
                    continue
                raw = _clean(token)
                nwords = len(raw.split())
                if raw and 1 <= nwords <= 6 and 2 < len(raw) <= 45 and raw not in STOPWORDS:
                    found.add(raw)
    return found


def render(words: set[str]) -> str:
    """Comma-separate, wrap to ~78 cols."""
    items = sorted(words)
    lines, cur = [], ""
    for i, w in enumerate(items):
        piece = w + ("," if i < len(items) - 1 else "")
        if len(cur) + len(piece) + 1 > 78:
            lines.append(cur.rstrip())
            cur = ""
        cur += piece + " "
    if cur.strip():
        lines.append(cur.rstrip())
    return "\n".join(lines)


def markers(name: str) -> tuple[str, str]:
    return f"<!-- SYNC:{name}:START -->", f"<!-- SYNC:{name}:END -->"


def current(text: str, name: str) -> str | None:
    start, end = markers(name)
    m = re.search(re.escape(start) + r"\n(.*?)\n" + re.escape(end), text, re.DOTALL)
    return m.group(1).strip() if m else None


def replace_block(text: str, name: str, new_body: str) -> str:
    start, end = markers(name)
    return re.sub(
        re.escape(start) + r"\n.*?\n" + re.escape(end),
        f"{start}\n{new_body}\n{end}",
        text,
        flags=re.DOTALL,
    )


def _parse_words(block: str, mode: str) -> set[str]:
    if mode == "word":
        return {w.strip() for w in re.split(r"[,\s]+", block) if w.strip()}
    return {p.strip() for p in block.split(",") if p.strip()}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true",
                    help="exit 1 if any block would change (staleness nudge)")
    ap.add_argument("--dry-run", action="store_true",
                    help="print new blocks, write nothing")
    ap.add_argument("--only", action="append", default=[],
                    help="restrict to block(s) by marker name (VOCAB/PUFFERY/COMMS); repeatable")
    args = ap.parse_args()

    if not PATTERNS.exists():
        print(f"error: {PATTERNS} not found", file=sys.stderr)
        return 2
    text = PATTERNS.read_text(encoding="utf-8")

    only = {s.upper() for s in args.only} or None
    blocks = [b for b in BLOCKS if not only or b["marker"] in only]
    if not blocks:
        print(f"error: no blocks match --only {sorted(only)}", file=sys.stderr)
        return 2
    for b in blocks:
        start, end = markers(b["marker"])
        if start not in text or end not in text:
            print(f"error: markers for {b['marker']} not found in {PATTERNS.name}",
                  file=sys.stderr)
            return 2

    try:
        wikitext = fetch(WIKI_URL)
    except Exception as e:  # network/timeout/decode — never crash the skill
        print(f"warning: fetch failed ({e}); leaving blocks unchanged", file=sys.stderr)
        return 0

    any_stale = False
    for b in blocks:
        scraped = extract(wikitext, b["hints"], b["mode"])
        words = b["baseline"] | scraped  # union: never shrink below baseline
        words -= b.get("rejected", set())  # honor curated rejections
        new_body = render(words)
        old_body = current(text, b["marker"])

        if args.dry_run:
            print(f"--- {b['marker']} ---")
            print(new_body)
            print()
            continue

        if new_body == old_body:
            if not args.check:
                print(f"{b['marker']}: up to date.")
            continue

        any_stale = True
        if args.check:
            added = words - _parse_words(old_body or "", b["mode"])
            detail = ", ".join(sorted(added)) if added else "(reflow only)"
            print(f"{b['marker']}: stale - {len(added)} new: {detail}", file=sys.stderr)
        else:
            text = replace_block(text, b["marker"], new_body)
            print(f"{b['marker']}: updated ({len(words)} entries).")

    if args.dry_run:
        return 0
    if args.check:
        return 1 if any_stale else 0
    if any_stale:  # we accumulated edits into `text`
        PATTERNS.write_text(text, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
