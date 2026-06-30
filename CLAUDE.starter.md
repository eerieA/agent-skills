<!--
  CLAUDE.starter.md — a baseline CLAUDE.md for a new coding/SWE project.

  HOW TO USE: Copy this to a project's root as CLAUDE.md, then PRUNE.
  - Rules 1–4 are project-agnostic; keep them verbatim unless you disagree.
  - Everything in [brackets] is a slot to fill or a section to delete.
  - When in doubt, delete. A short, true CLAUDE.md beats a long one with
    stale or irrelevant instructions — every line competes for attention.
  - Delete this comment block once you've adapted the file.
-->

# CLAUDE.md

## Project Purpose

A project that [insert one-sentence project introduction].

> [Optional: a top-level note about what the project is or is NOT — scope
> boundaries, a key constraint, or a "don't do X here" warning. Delete if unneeded.]

## Behavioral guidelines

[Recommended default working agreement for coding agents. Rules 1–4 apply to
almost any project; keep them. Edit or delete rule 5 to match your stack.]

### 1. Think Before Coding

**Don't assume. Don't hide confusion. Surface tradeoffs.**

Before implementing:
- State your assumptions explicitly. If uncertain, ask.
- If multiple interpretations exist, present them - don't pick silently.
- If a simpler approach exists, say so. Push back when warranted.
- If something is unclear, stop. Name what's confusing. Ask.

### 2. Simplicity First

**Minimum code that solves the problem. Nothing speculative.**

- No features beyond what was asked.
- No abstractions for single-use code.
- No "flexibility" or "configurability" that wasn't requested.
- No error handling for impossible scenarios.
- If you write 200 lines and it could be 50, rewrite it.

Ask yourself: "Would a senior engineer say this is overcomplicated?" If yes, simplify.

### 3. Surgical Changes

**Touch only what you must. Clean up only your own mess.**

When editing existing code:
- Don't "improve" adjacent code, comments, or formatting.
- Don't refactor things that aren't broken.
- Match existing style, even if you'd do it differently.
- If you notice unrelated dead code, mention it - don't delete it.

When your changes create orphans:
- Remove imports/variables/functions that YOUR changes made unused.
- Don't remove pre-existing dead code unless asked.

The test: Every changed line should trace directly to the user's request.

### 4. Goal-Driven Execution

**Define success criteria. Loop until verified.**

Transform tasks into verifiable goals:
- "Add validation" → "Write tests for invalid inputs, then make them pass"
- "Fix the bug" → "Write a test that reproduces it, then make it pass"
- "Refactor X" → "Ensure tests pass before and after"

For multi-step tasks, state a brief plan:
```
1. [Step] → verify: [check]
2. [Step] → verify: [check]
3. [Step] → verify: [check]
```

Strong success criteria let you loop independently. Weak criteria ("make it work") require constant clarification.

### 5. Design Standard

**Hold non-trivial code to a consistent design standard.**

[OPTIONAL — fill in if this project has a design-discipline skill or doc to
defer to, otherwise delete this rule. Point at whatever applies to THIS project:]

When writing or reviewing non-trivial code — deciding where logic belongs,
structuring a feature, naming it, drawing a boundary against an API, or layering
validation and errors — consult [the `[skill-or-doc-name]` skill / `[path/to/doc]`].
It reinforces rules 2 and 3 above (simplicity, surgical changes).

## Project-Specific Conventions

[OPTIONAL — capture the few non-obvious, project-specific rules an agent can't
infer from the code itself. Delete the lines that don't apply. Keep this short;
anything obvious from reading the codebase does NOT belong here.]

- **Build / run:** [e.g. `npm run dev`, `make build`]
- **Test:** [e.g. `pytest -q`, `npm test`; note which tests to run before claiming done]
- **Lint / format:** [e.g. `ruff check`, `prettier --write`; run before finishing]
- **Commits / PRs:** [e.g. conventional commits; never push to main; branch naming]
- **Gotchas:** [anything that will silently bite — env setup, codegen step, etc.]

## Project Knowledge Base Files

[OPTIONAL — list reference docs the agent should read for deeper context, and
WHEN to read each. Delete this whole section if the project has no such docs.]

### [Knowledge base group 1 — e.g. "Domain / spec docs"]
Read these when [insert the trigger — e.g. "working on the data model or API contract"].

**Caveat:** [Optional — pitfalls or warnings, e.g. "these describe the spec we
follow but do NOT modify; treat as read-only reference."]

| Path | Contents |
|---|---|
| `docs/[file01].md` | [one-line summary] |
| `docs/[file02].md` | [one-line summary] |

<!--
  TIP for long files: when a doc is large, note section offsets so the agent
  can read with `offset` instead of truncating. Example row:
  | `docs/big.md` | API reference | 1217 lines — §16 at line 932, §20 at line 1138 |
  Add a "Size / section offsets" column like the above only if you have such files.
-->
