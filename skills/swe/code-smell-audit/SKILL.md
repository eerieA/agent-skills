---
name: code-smell-audit
description: >
  Code smell audit and refactoring skill. Scans a codebase (or specified files)
  for silent fallbacks, dead code, missing guards, hardcoded external names,
  order-dependent behavior, duplicated sources of truth, and
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

### 8. No-op wrapper — identity logic dressed up as work (Medium)

A function (or block) whose branches all collapse to the same trivial result the caller
could get directly, but whose name, comment, or type signature claims it does something
meaningful. The ceremony impersonates logic: a reader trusts the name and assumes a
guard, a transform, or a side effect is happening when nothing is.

The canonical shape is an identity function — every path returns its own input unchanged:

```
// returnRowErrorOnTxFailure returns the error from in-transaction work so the row
// fails and processing does not continue.
func returnRowErrorOnTxFailure(err error) error {
    if err == nil {
        return nil
    }
    return err
}
```

Both branches return `err` (when `err` is nil, `err` *is* nil) — the whole function is
`return err`. The comment promises control-flow significance the code does not provide.

Look for:
- Functions where every `return`/branch yields the input unchanged (`return err`,
  `return x`, `if v: return v else: return v`)
- A wrapper that only forwards its argument with no added context, validation, logging,
  or transformation
- A name or comment asserting behavior ("ensures…", "so that…", "guards against…") that
  the body does not actually implement
- Conditionals whose arms produce identical results (`if c: return a else: return a`)

**Fix pattern:** delete the wrapper and use the value directly at the call sites. If the
wrapper was *meant* to do something (add context to the error, log, validate), make it
actually do that — e.g. wrap with `fmt.Errorf("tx failed: %w", err)` — so the name
becomes true. Never keep a no-op whose only output is a misleading name.

---

### 9. Order-dependent behavior over an unordered collection (High)

Code whose *result* depends on the order in which items are processed, but which iterates
a collection with no guaranteed order — a hash map/set, a query without `ORDER BY`, a
parallel reduce, filesystem listing, or an event-handler list built in registration
order. It works on the author's machine because the order happens to be stable there,
then silently produces a different result under a different runtime, dataset size, or
platform. The same failure class covers unseeded randomness used where a reproducible
sequence is needed.

The tell is that reordering the inputs would change the output, yet nothing pins the order:

```python
# Applies discounts by iterating a dict — insertion order is not the domain order.
for rule in discount_rules.values():   # order is incidental, not intended
    price = rule.apply(price)          # non-commutative: order changes the result
```

If `discount_rules` were built differently, `price` would differ — with no error.

Look for:
- Iteration over a `set`/`dict`/hash map where the loop body accumulates, mutates shared
  state, or emits output in that order
- A DB query feeding ordered output or "first match" logic with no `ORDER BY`
- Reductions/merges of results gathered concurrently (thread pool, `Promise.all`,
  goroutines) where combination is not commutative
- "First one wins" / "last one wins" resolution over an unordered source
- `random(...)` / `shuffle(...)` without a seed in code that must reproduce (tests,
  simulations, fixtures) — see the fuzz/property-testing note in the testing skill

**Fix pattern:** sort explicitly by a stable, meaningful key at the point of iteration
(`sorted(rules, key=...)`, `ORDER BY`), or use an ordered container if insertion order
*is* the intended contract — and say so in a comment. For randomness that must repeat,
thread an explicit seed through. The test: if reordering the input can change the output,
the order must be pinned deliberately, not inherited by accident.

---

### 10. Duplicated source of truth that can silently drift (Medium)

The same fact — an enum value, a route path, a config key, a type's field list, a status
name — is written out by hand in two or more places that must stay in agreement, with
nothing enforcing it. When one copy is updated and the others aren't, the mismatch does
not fail loudly; it produces a subtle wrong-mapping bug far from either edit site.

```
// Declared here…
enum ComponentType { Bleed, Poison, /* ... */ };

// …and the name repeated by hand there — update one, forget the other, silent drift.
REGISTER_COMPONENT(Bleed, "bleed");   // string "bleed" must match the enum, but nothing checks
```

Look for:
- A name/value duplicated across an enum and a lookup table, a constant and a string key,
  a type and its (de)serializer, a route constant and its handler registration
- Parallel lists that must line up by position or by name across files
- "Add a new X in three places" steps in a README or comment — a standing drift hazard
- Copy-pasted blocks that encode the same fact, where updating one but not the rest breaks
  a mapping rather than raising an error

**Fix pattern:** make one place the source of truth and derive the rest — generate the
table from the enum (codegen/build step), read the key from the single constant, drive
(de)serialization from the type. Where full derivation is overkill, add a compile-time or
startup assertion that the copies agree, so drift fails loudly instead of silently. Don't
add a heavy abstraction for a single pair — a check that they match may be enough.

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
