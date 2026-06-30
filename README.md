# agent-skills

Personal collection of reusable [Claude Code](https://claude.com/claude-code) assets - skills and a CLAUDE.md starter - to drop into coding/SWE projects.

## Contents

### `CLAUDE.starter.md`
A baseline `CLAUDE.md` for a new project. It's a starter, not a template: copy it to a project root as `CLAUDE.md`, then prune. Bracketed `[...]` slots get filled or deleted; the default working agreement (rules 1–4) is project-agnostic and meant to stay. When in doubt, delete.

### `skills/`
Skills usable via the `Skill` tool or a `/slash-command`, grouped by domain (`swe/` for software work; future domains get their own folder).

| Skill | What it does |
|---|---|
| `swe/code-smell-audit` | Code-smell audit and refactor - scans for silent fallbacks, dead code, missing guards, and other reliability anti-patterns, then fixes what you approve. Invoke with `/code-smell-audit`. |
| `swe/gql-frontend-arch` | Architecture guidance for a frontend web app on a GraphQL backend - module boundaries, state/data-fetching, where logic lives, the API seam, tables, forms, and testing strategy. |

## Usage

- **Starter:** copy `CLAUDE.starter.md` → `<project>/CLAUDE.md`, then adapt and delete the leading comment block.
- **Skills:** copy the individual skill subfolder into a project's `.claude/skills/` - e.g. `skills/swe/code-smell-audit/` → `<project>/.claude/skills/code-smell-audit/` - then invoke by name. The `swe/` grouping is for organizing this repo; it isn't part of the invocation path.
