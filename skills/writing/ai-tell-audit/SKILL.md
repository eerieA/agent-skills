---
name: ai-tell-audit
description: >
  Audit prose for AI writing tells and advise fixes, without rewriting behind the
  writer's back. Point it at a draft, doc, README, memory file, UI copy, or any
  paste; it scans for the giveaways that mark text as machine-generated: puffery and
  significance inflation, promotional tone, formulaic structures (rule of three,
  "not X but Y", "Despite challenges"), stylistic quirks (elegant variation, false
  ranges, copula avoidance), formatting tells (em dashes, mechanical boldface, title
  case), and voiceless "clean but soulless" prose. Tiered by severity with a strong
  false-positives guard so it flags clusters, not lone coincidences, and never
  flattens legitimate human writing. Produces a prioritized findings table, then
  fixes only what the writer approves. Invoke with /ai-tell-audit.
metadata:
  domain: writing
  scope: review
  output-format: findings-table
---

Review prose for the patterns that make text read as AI-generated, and propose
targeted fixes. This is a **detect-and-advise** skill: find concrete tells, rank
them, and let the writer decide what to change. Do not rewrite the whole piece,
impose a house voice, or "improve" prose that is already fine.

The governing idea: an AI tell is a *statistical* habit - the most likely phrasing
that fits the widest range of cases. One such phrasing proves nothing (humans write
that way too). A **cluster** of them is the confession. So this skill is biased
toward restraint: it always flags the unambiguous tells, flags the softer ones only
when they pile up, and treats the false-positives guard as a first-class rule, not a
footnote.

## Intake

Ask the writer to provide the text (paste, file path, or a range) and, if not
obvious:
- **Register** - is this meant to be technical/reference, casual/personal, marketing,
  or fiction? The bar moves: neutral plainness is *correct* for reference docs but a
  tell in a personal essay (see voice, below).
- **Provenance** - is this their own writing they want checked, or AI output they
  want cleaned up? Be gentler and more cluster-driven on the former; over-editing a
  human's real voice is the worst failure mode here.

If they don't specify, assume technical/reference and lean conservative.

## Severity tiers

The tier decides *when* you flag, not just how loud.

| Tier | Meaning | Flagging rule |
|------|---------|---------------|
| **High** | Unambiguous tell; rarely appears in careful human prose | Flag every instance, standalone |
| **Medium** | Real tell, but also a normal human habit in isolation | Flag only in a **cluster** (2+ tells near each other, or a repeated pattern) |
| **Voice** | Not a "wrong phrase" - the text is clean but soulless | Flag only when register is expressive (essay, blog, personal, marketing), never for reference/technical text |

When in doubt on a Medium item, **don't flag it** - note it silently and see whether
the cluster forms. A lone em dash, one "however", one curly quote: not a finding.

**Exception - citations.** Citation hallucination (`craft/bad-citation.md`) inverts
the cluster rule: a *single* malformed reference (checksum-invalid ISBN, wrong-paper
DOI, author dead at the cited date) is High evidence standalone, because humans
almost never fabricate one. Flag those on first hit.

## Audit workflow

1. Read the text once for register and overall voice before hunting patterns.
2. Scan against the catalogs in `craft/`:
   - `craft/patterns.md` - the tell catalog, grouped **wording / structure / voice &
     tone / formatting**, each with before → after.
   - `craft/bad-citation.md` - citation hallucination (invalid ISBN/DOI, wrong-paper
     DOI, page-less cites, impossible author/date). A *verification* tell, not a
     surface one, and the one place the cluster rule inverts - see below. Consult
     only when the text carries references.
   - `craft/false-positives.md` - what is **not** a tell. Consult this *before*
     writing any finding; it is the over-correction guard.
   - `craft/examples.md` - worked before/after transformations for the harder cases.
3. Optionally run the regex pre-screen (see Tooling) to catch the mechanical tells
   fast, then apply judgment on top - the script finds candidates, it does not decide.
4. For each surviving finding, record:
   - **Location** - file:line, quote, or paragraph marker
   - **Severity** - High / Medium / Voice
   - **Tell** - which pattern (name it from `craft/patterns.md`)
   - **Why it reads as AI** - the concrete problem, one line
   - **Suggested fix** - a specific replacement or direction, not "make it better"
5. Present findings as a markdown table grouped by severity, most severe first.
6. Ask which findings to address. Fix only those, one at a time, showing before/after.

## Fixing (only after approval)

- **Rewrite, don't delete.** Cover everything the original covered. If a paragraph
  had five points, the fix keeps five points - it just drops the tell.
- **Preserve meaning and register.** Match the writer's voice, don't upgrade their
  vocabulary. If they write "stuff", don't make it "elements".
- **Preserve exactly** - never touch: fenced/inline code, URLs and links, file paths,
  commands, env vars, version numbers, dates, proper nouns, tables' structure, YAML
  frontmatter, and headings' text. Tells live in prose *between* these; the technical
  substrate is read-only.
- **Don't over-correct.** Removing a tell should make the sentence more direct, not
  more generic. If your fix sounds blander than the original, the original was fine.

## Tooling

`scripts/sync-wikipedia.py` - optional. Refreshes the vocabulary/phrase block in
`craft/patterns.md` from Wikipedia's "Signs of AI writing" page, so the catalog does
not drift as the community guide evolves. The skill works fully without ever running
it; run it when you suspect the vocab list has gone stale. It updates only the
marked, auto-generated block and leaves the hand-written patterns untouched.

A lightweight regex pre-screen can be added later against the same block; for now the
scan is judgment-driven against `craft/`.

## What this skill will not do

- Rewrite the whole piece unprompted, or restructure beyond removing tells.
- Flag a single Medium tell as if it were proof.
- Detect model-specific artifacts (e.g. leaked search-tool tokens). Those churn with
  model releases and belong in a linter, not a durable writing skill.
- Score prose for "AI probability". These are signs, not proof - the output is a
  findings list a human acts on, not a verdict.
