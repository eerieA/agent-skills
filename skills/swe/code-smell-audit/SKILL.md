---
name: code-smell-audit
description: >
  Code smell audit and refactoring skill. Scans a codebase (or specified files)
  for silent fallbacks, dead code, missing guards, hardcoded external names, and
  other reliability anti-patterns. Produces a prioritized findings table, then
  fixes what the user approves. Invoke with /code-smell-audit.
---

Perform a focused reliability audit of the current codebase (or files the user names).
Do not refactor style, rename things, or change logic beyond what is needed to fix each
finding. Match existing code style exactly.

## Audit checklist

Work through each category below. For each finding, record:
- **File:line** — exact location
- **Severity** — High / Medium / Low (see definitions)
- **Pattern** — which smell (use the names below)
- **What goes wrong** — the failure mode, not just the smell name
- **Suggested fix** — one-line description

Present findings as a markdown table, grouped by severity. After the table, ask the
user which findings to fix before touching any code.

---

### 1. Silent fallbacks (High)

Code that substitutes a default value when an external lookup returns nothing, instead
of raising. The caller receives plausible-looking data and continues, propagating the
bad state far from the source.

Look for:
- `x or "default_string"` / `x or 0` / `x or []` after an API/DB call result
- Functions that `return ""` / `return None` / `return some_const` on lookup failure
  when callers depend on the value being real
- `getattr(obj, "field", "fallback")` on objects from external systems
- `except Exception: return default` swallowing lookup errors
- Conditional branches where the else arm silently skips required work

**Fix pattern:** raise a `ValueError` (or domain-appropriate exception) with a message
that names the missing object and the query used to find it.

---

### 2. Missing None guards before attribute access (High)

External API calls that return `None` on miss, followed immediately by attribute access
without a None check. Produces an `AttributeError` with no context about what was
missing or why.

Look for:
- `result = api.get(...)` followed by `result.field` without `if result is None`
- Chained access like `obj.nested.field` where `nested` comes from an external call
- `for item in api.filter(...)` where the iterable could be None rather than empty

**Fix pattern:** add an explicit `if x is None: raise ValueError(f"<Object> not found: {query!r}")`
immediately after the lookup, before any attribute access.

---

### 3. Hardcoded external names (Medium)

String literals that must match names in an external system (database, API, config) exactly.
A rename in the external system silently breaks the code — often returning None rather
than an error.

Look for:
- String literals passed directly to `.get(name=...)` / `.filter(name=...)`
- Interface names, role slugs, tag slugs, group names, VlanGroup names embedded as
  string constants in business logic
- Magic strings repeated in multiple files (drift risk if one is updated and another isn't)

**Fix pattern:** prefer tag/slug-based discovery over name-based lookup where the API
supports it. If a name must be used, centralise it as a named constant at module level
and add a comment explaining the external coupling. Do not invent an abstraction — one
constant per coupling is enough.

---

### 4. Dead code — unused results (Low)

A call whose return value is never used. Wastes a round-trip and misleads readers into
thinking the result matters.

Look for:
- `result = expensive_call(...)` where `result` is never read afterward
- `_ = api.get(...)` or bare `api.get(...)` where the return value is silently dropped
- Variables assigned inside a branch and never referenced outside it

**Fix pattern:** delete the call entirely if the side-effect is not needed. If the call
is needed for its side-effect, add a comment explaining why.

---

### 5. Wrong return-type on partial failure (High)

A function whose docstring or type annotation says it returns `X`, but on certain failure
paths it silently returns `None`, `""`, or a different type. Callers written against the
declared type will crash or misbehave.

Look for:
- Functions annotated `-> str` that have `return None` paths
- Functions annotated `-> list[X]` that return `None` instead of `[]`
- Functions annotated `-> SomeDataclass` that return a partially-populated instance
  when a required field could not be resolved

**Fix pattern:** either make the return type honestly nullable (`-> str | None`) and
handle None at every call site, or raise on the failure path instead of returning a
wrong-typed value.

---

### 6. Type-narrowing bypass (Medium)

Code that checks a value for None or a sentinel, then passes the unchecked value into
a call that assumes it is non-None.

Look for:
- `if x: use(x.field)` where `x` could be a non-None falsy value (empty string, 0)
  and the intent was a None check
- `x and x.field or default` — short-circuits but leaves the type ambiguous
- `assert x is not None` in production code (hides a real validation gap)

**Fix pattern:** use explicit `if x is None` / `if x is not None` rather than truthiness
checks when the value comes from an external system.

---

### 7. Exception swallowing (High)

A `try/except` that catches a broad exception class and either silences it entirely or
converts it to a silent default.

Look for:
- `except Exception: pass`
- `except Exception: return None` / `return {}`
- `except (TypeError, AttributeError, KeyError): continue` inside a loop that
  processes external data

**Fix pattern:** catch only the specific exception you expect. Log or re-raise
unexpected exceptions. If None is a valid return, make that explicit in the type and
document why.

---

## Severity definitions

| Severity | Meaning |
|----------|---------|
| High | Can produce wrong data delivered to the caller, or an uncontrolled crash with no context |
| Medium | Creates maintenance risk or future breakage but does not currently corrupt data |
| Low | Wasted work or misleading code; no current failure risk |

---

## After presenting findings

1. Show the findings table.
2. Ask: "Which findings should I fix? (e.g. 'all High', 'items 1 3 5', 'skip dead code')"
3. Fix only what the user approves — one finding at a time, show the diff.
4. Do not touch adjacent code, formatting, or naming unless the fix requires it.
