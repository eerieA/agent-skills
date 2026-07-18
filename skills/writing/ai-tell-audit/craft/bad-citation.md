# Citation hallucination

A different kind of tell from everything in `patterns.md`. Those are **surface**
tells - you spot them by reading the prose. This is a **verification** tell - you
can't see it by reading; you check the reference against the world.

The cluster rule that governs the rest of this skill is **inverted here**. A single
fabricated-looking reference is strong evidence on its own, because humans almost
never produce a citation that is internally malformed (a checksum-invalid ISBN, a
DOI pointing to a different paper, an author dead at the claimed publication date).
People miscite, but they rarely manufacture a plausible-looking source from nothing.
So most checks below are **High, standalone** - flag on the first hit.

## How to run it

Default to **static inspection** - no network. Flag suspects from the text alone,
then offer to verify:

> N citation suspects found. Want me to resolve the DOIs and check the links live?

Only fetch/resolve on request. This keeps the audit fast and dependency-free by
default; live verification is opt-in per run.

## Static checks (no network)

### 1. Invalid ISBN checksum - High
ISBNs carry a check digit. An invalid checksum means the number was never a real
ISBN - a near-certain fabrication tell.

- ISBN-13: sum of digits × alternating 1,3 weights must be ≡ 0 (mod 10).
- ISBN-10: sum of digit × position (10..1) must be ≡ 0 (mod 11); final digit may be
  `X` = 10.
- Before: *Introduction to Electric Circuits ... ISBN 9780470521572* (checksum fails)
- Action: flag as likely hallucinated; the real book may exist, but this number is
  wrong.

### 2. Impossible author / date - High
Internal facts that can't be true: an author dead years before the cited publication,
a journal volume/issue that predates the journal, a "2024" source cited in a 2019
document.

- Before: *C. L. Fortescue, Proceedings of the IEEE, 1974* - Fortescue died in 1936.
- Action: flag; a real citation can't be authored posthumously by 38 years.

### 3. Page-less book citation backing a specific claim - Medium
A book cite with no page/section number can't verify the specific sentence it's
attached to. Common AI move: attach a real, plausible book to a precise claim
without the locator that would let anyone check it.

- Before: *...a cornerstone of circuit analysis [1].* / *[1] Dorf & Svoboda,
  Introduction to Electric Circuits (8th ed.).* (no page)
- Action: flag Medium; ask for the page, or treat the claim as unsupported.

### 4. Citation-count / density mismatch - Medium (cluster)
A short passage with a citation after nearly every sentence, or a reference list far
longer than the prose warrants, is a synthesis-shaped tell - especially combined with
any check above. Flag only alongside another signal.

### 5. Formatting incoherence in the reference block - Low
Curly quotes in some references but straight in others; inconsistent template style;
a mix of citation formats within one list. Weak alone (see `false-positives.md` on
curly quotes); counts only as corroboration.

## Live checks (only when the writer opts in)

### 6. Unresolvable DOI - High
A DOI that does not resolve (via `https://doi.org/<doi>`) is very likely invented.
DOIs are far more rot-resistant than plain URLs, so a dead DOI rarely means link rot.

### 7. DOI resolves to the WRONG paper - High
The DOI resolves, but to a different title/author/journal than the citation claims.
This is the subtle case static checks can't catch: the reference looks perfect and
even resolves, but points somewhere unrelated. Compare resolved metadata to the cited
title/author/year.

### 8. Dead external links - Medium (High in a cluster)
A 404 link is ordinary link rot on its own. But if **most** links in a new document
are dead AND absent from the Internet Archive / Archive.today, that pattern suggests
they were never valid - a strong AI-generation signal in aggregate.

## Explicitly out of scope (churn - belongs in a linter, not this skill)

These appear in the source material but are model- or platform-specific and drift
with releases, so they are deliberately excluded here - the same call made for
model-artifact detection elsewhere in the skill:

- `utm_source=openai` / `utm_source=chatgpt.com` on source URLs.
- The `↩` footnote glyph from certain chatbot UIs.
- Wikitext-specific errors: hallucinated `[[Category:...]]`, malformed `<ref>` reuse
  syntax. (These are Wikipedia-editing tells, not general-writing tells.)

If you need those, put them in a mechanical pre-commit linter. Keeping them out of
this file is what stops the skill from going stale and narrow.

## Fixing

Never silently "fix" a citation by inventing a corrected one - that manufactures the
exact problem being audited. The only valid fixes:
- Replace with a real source the writer supplies or you verify resolves correctly.
- Downgrade the claim to unsupported ("no citation found") and let the writer source
  it.
- Remove the fabricated reference and the claim that depended on it.
