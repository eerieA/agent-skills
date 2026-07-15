# agent-skills

Personal collection of reusable [Claude Code](https://claude.com/claude-code) assets - skills and a CLAUDE.md starter - to drop into coding/SWE and other types of projects.

<!-- TOC -->

- [agent-skills](#agent-skills)
    - [Contents](#contents)
        - [`CLAUDE.starter.md`](#claudestartermd)
        - [`skills/`](#skills)
            - [Software](#software)
            - [UI/UX](#uiux)
            - [Writing](#writing)
    - [Usage](#usage)

<!-- /TOC -->

## Contents

### `CLAUDE.starter.md`
A baseline `CLAUDE.md` for a new project. It's a starter, not a template: copy it to a project root as `CLAUDE.md`, then prune. Bracketed `[...]` slots get filled or deleted; the default working agreement (rules 1–5) is project-agnostic and meant to stay. When in doubt, delete.

### `skills/`
Skills usable via the `Skill` tool or a `/slash-command`, grouped by domain (`swe/` for software work, `uiux/` for interface design; future domains get their own folder).

#### Software

| Skill | What it does |
|---|---|
| `swe/code-smell-audit` | Code-smell audit and refactor - scans for silent fallbacks, dead code, missing guards, and other reliability anti-patterns, then fixes what you approve. Invoke with `/code-smell-audit`. |
| `swe/cicd-pipeline` | Platform-agnostic CI/CD deployment pipeline design and review - stage flow, approval and metric gates, choosing a rollout strategy (rolling/blue-green/canary/feature-flag), safe rollback with backward-compatible migrations, health checks that don't lie, and build-once-promote-the-same-artifact. Applies to any runner and any target; ends with a design-review checklist. |
| `swe/gql-frontend-arch` | Architecture guidance for a frontend web app on a GraphQL backend - module boundaries, state/data-fetching, where logic lives, the API seam, tables, forms, and testing strategy. |
| `swe/react-best-practices` | Senior-level guidance for building and reviewing production React + TypeScript - component architecture, hooks, state management (Context, Redux Toolkit, TanStack Query), performance, Server Components, testing, and UI/interaction polish. |
| `swe/safe-refactor` | Language- and framework-agnostic refactoring discipline - restructuring code without changing behavior via the safety loop (small steps, tests green after each, commit rhythm), when NOT to refactor, and a catalog of concrete refactoring operations. |
| `swe/testing-discipline` | Language- and framework-agnostic testing discipline - test-first / prove-it-with-a-failing-test workflow, what makes a test good, how to size a suite (unit/integration/e2e), and fuzz/property testing for combinatorial systems with reproducible seeds. |

> `swe/safe-refactor` is recommended to be used together with `swe/code-smell-audit` (to find what to change) and `swe/testing-discipline` (for the tests the safety loop leans on), but it works standalone and requires neither.

#### UI/UX

| Skill | What it does |
|---|---|
| `uiux/ux-principles` | Framework- and style-agnostic UX discipline - the durable heuristics that decide whether an interface *works*: visual hierarchy, chunking, Gestalt grouping, scale/contrast/signal-to-noise, a decision toolkit of UX laws (Hick, Fitts, Miller, Jakob, Doherty, Peak-End, and more), progressive disclosure, forgiveness, full interaction-state cycles, and accessibility as a floor. Applies to any surface - marketing, product, dashboard, form. |
| `uiux/ui-design` | Anti-slop *visual* UI design for product and marketing surfaces. Reads the brief instead of defaulting to a templated look, then builds around a normalized **style contract**. The aesthetic is pluggable: pick a built-in style (`minimalist`, `brutalist`), describe your own, hand over a reference image, or let it infer one. Enforces style-independent invariants (WCAG contrast, touch targets, reduced-motion, theme/accent/shape locks, real images over fake screenshots) that no style may override, plus an AI-tells catalog and a pre-flight check. |

> `uiux/ux-principles` (does it *work*) and `uiux/ui-design` (how it *looks and feels*) are designed to pair, but each works standalone and requires neither the other nor any framework skill. New visual styles for `ui-design` are pluggable: drop a style pack into `uiux/ui-design/styles/` following `_template.md`.

#### Writing

| Skill | What it does |
|---|---|
| `writing/world-building` | Interactive fiction world-building - interviews you to build a coherent story world (genre-aware), enforces rules-generate-conflict and "the world is not the story" discipline, then suggests a world-bible structure. Invoke with `/world-building`. |
| `writing/world-audit` | Audit an existing fiction world - scans your notes, bible, or draft for missing rules, contradictions, unbounded magic/tech, infodump risk, and thin sensory detail, then fixes what you approve. Invoke with `/world-audit`. |
| `writing/character-building` | Interactive fiction character-building - interviews you to build one character in depth or a whole cast web, centering the want-vs-need contradiction, the ghost and lie, and revelation through choice under pressure. Invoke with `/character-building`. |
| `writing/character-audit` | Audit existing fiction characters - scans your profiles, notes, or draft for want-without-need, flat/too-perfect/too-evil characters, obstacle-only opponents, dumped characterization, and dialogue without subtext, then fixes what you approve. Invoke with `/character-audit`. |

## Usage

- **Starter:** copy `CLAUDE.starter.md` → `<project>/CLAUDE.md`, then adapt and delete the leading comment block.
- **Skills:** copy the individual skill subfolder into a project's `.claude/skills/` - e.g. `skills/swe/code-smell-audit/` → `<project>/.claude/skills/code-smell-audit/` - then invoke by name. The `swe/` and `writing/` groupings are for organizing this repo; they aren't part of the invocation path.
- **`references.md` is author-only.** When a skill folder contains a `references.md`, it's a memory-jog recording what the skill was built on - not part of the skill. Leave it out when copying a skill into a project.
