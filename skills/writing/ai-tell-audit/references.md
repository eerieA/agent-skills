# Sources

Personal notes on what this skill was built from. Not copied when the skill is
imported into a project — this is a memory-jog for the author, not part of the skill.

The skill distills these sources; it does not reproduce them. Follow the links /
titles below to the originals.

| Source | What it contributed |
|---|---|
| [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) (WikiProject AI Cleanup) | The backbone taxonomy: puffery/significance inflation, promotional tone, superficial -ing analyses, vague attribution, rule of three, elegant variation, false ranges, copula avoidance, formatting tells. Also the "signs, not proof" framing and the live vocabulary list that `scripts/sync-wikipedia.py` refreshes. |
| [blader/humanizer](https://github.com/blader/humanizer/blob/main/SKILL.md) | The richest before/after pattern catalog (33 patterns) — most of `craft/patterns.md`'s entries and examples trace here. Two ideas taken wholesale: the **voice / "clean but soulless"** tier (C-group) and the strong **false-positives / detection-guidance** section that became `craft/false-positives.md`. Also the "rewrite don't delete, cover everything the original covered" fix rule. |
| [unslop-file](https://github.com/sickn33/agentic-awesome-skills/blob/808bdee2a0da597643889b6f1a9c4a961609c73a/skills/unslop-file/SKILL.md) | The **preserve-exactly** contract (code, URLs, paths, commands, frontmatter are read-only) and the compact Remove / Tighten / Preserve rule shape. Its deterministic/LLM two-mode idea was noted but *not* adopted — this skill is detect-and-advise, not file-mutating. |
| [Hardik Pandya, stop-slop](https://github.com/hardikpandya/stop-slop/blob/main/SKILL.md) | The structural model copied here: thin dispatcher SKILL.md + focused sub-files. Its structure-patterns file fed B-group (binary contrasts, negative listing, dramatic fragmentation, false agency, narrator-from-a-distance) and the quick-check discipline. |
| [ai-anti-patterns](https://github.com/edwinhu/workflows) | The **severity-tier** organization (High/Medium, here extended with a Voice tier) and the single-source **sync-script** idea. Its citation-problems reference became `craft/bad-citation.md` — the **durable core** (invalid ISBN/DOI, wrong-paper DOI, page-less cites, impossible author/date, dead-link clusters), the one check where the cluster rule inverts (a lone bad citation is High standalone). Deliberately *not* adopted: its per-section sync-script sprawl (collapsed to one narrow script), model-specific artifact detection like `turn0search0`/`oaicite`, and the churny citation bits (`utm_source=openai`, `↩` footnote glyph, wikitext `[[Category:]]`/`<ref>` syntax) — all linter territory, not durable writing tells. |

Design decisions worth remembering:
- **Detect + advise, not rewrite** — the whole skill is biased toward restraint; the
  worst failure mode is flattening a real human voice.
- **Cluster rule** — Medium/Low tells flag only when they pile up. High tells flag
  standalone. This lives in both `SKILL.md` tiers and `craft/false-positives.md`.
- **Voice tier is register-gated** — soullessness is a tell for essays, correct for
  reference docs.

This skill sits under `skills/writing/` next to the `-audit` skills (`character-audit`,
`world-audit`) and mirrors their findings-table format. Its proactive counterpart —
a `CLAUDE.starter.writing.md` root-instruction template — is planned separately.
