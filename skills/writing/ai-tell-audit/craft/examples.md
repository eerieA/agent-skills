# Worked examples

Longer before/after transformations for the harder cases, where the fix is more than
a phrase swap. Each shows the *cluster* being removed, not one tell in isolation.

---

## 1. Promotional travel prose → honest recap (expressive register)

Multiple High + Voice tells at once: significance inflation, promotional tone, forced
enthusiasm, em dashes, rule-of-three, generic upbeat close, emoji.

**Before**
> Nestled along the banks of the Tagus, Lisbon stands as a vibrant testament to
> Portugal's enduring spirit, where rich history and modern energy intertwine at
> every turn. The hills are challenging - my legs certainly felt it! - but every
> climb rewards you with breathtaking, panoramic views. Would I go back? Absolutely.
> Lisbon isn't just a place to visit - it's a place to fall in love with. ✨

**After**
> I spent five days in Lisbon last October and still have mixed feelings. Beautiful,
> yes. Also harder on the knees than anyone warned me. My hotel was up in Alfama,
> which photographs well and meant climbing what felt like a six-story staircase
> every time I wanted coffee. By day two I was planning each walk around which way
> was downhill. I'd go back, but in spring and with better shoes.

Note what was *kept*: first person, concrete detail (Alfama, the staircase), mixed
feeling. The fix removed the tells without flattening the voice.

---

## 2. Puffed encyclopedia entry → neutral fact (reference register)

Cluster: copula avoidance, significance inflation, superficial -ing tail, vague
attribution.

**Before**
> Serving as a focal point of regional identity, the market stands as an enduring
> testament to local craftsmanship, drawing visitors from across the region and
> highlighting the community's deep connection to tradition. Experts believe it
> plays a vital role in the local economy.

**After**
> The market operates every Saturday and sells produce, textiles, and livestock. A
> 2019 municipal survey attributed about 12% of the town's retail activity to it.

Here the correct voice *is* neutral - no personality added, just tells removed and a
real figure substituted for the vague authority.

---

## 3. Documentation narrating a diff → describing the thing

Cluster: diff-anchored writing, negative parallelism.

**Before**
> This helper was introduced to replace the old loop-based lookup, which wasn't
> scalable - it's not just faster, it's the foundation the new cache is built on.

**After**
> This helper looks entries up through a hash map, giving O(1) access. The cache
> layer depends on it.

The doc now reads coherently without knowing what the last commit changed.

---

## 4. Chatbot residue in pasted content

Cluster: sycophancy, collaborative artifact, signposting.

**Before**
> Great question! Let's dive into the French Revolution. Here's what you need to
> know. I hope this helps - let me know if you'd like me to expand any section!

**After**
> The French Revolution began in 1789, when financial crisis and food shortages fed
> widespread unrest.

---

## 5. Over-explained engineering doc → same content, half the clauses

The E-group cluster, in a planning doc for a fictional web client. Note what is *not*
wrong here: no puffery, no vocabulary tells, no promotional tone. Every sentence is
accurate and the technical content is good. It still reads as machine-written, because
no claim is allowed to stand by itself.

**Before**

> `src/auth/user.ts`. DESIGN-07 pins the break site exactly right: `getUser()` does
> `TIERS.includes(id) ? id : 'owner'`, so once `id` is a person that test is false and
> **every user falls through to `owner`**. That is a display bug rather than a data-loss
> bug, since `permissions.ts` is explicit the client is not a security boundary - and it
> is what makes the `/current-user` call mandatory.
>
> **Decision to make: what renders before `/current-user` resolves.** Rendering the shell
> against a not-yet-known permission set flashes controls off then on; blocking on a
> splash costs a gate we don't have today. **Recommend blocking** - one round-trip on an
> internal tool, and it avoids showing controls the user may not have.
>
> Two viable shapes; pick one when building:

**After**

> `src/auth/user.ts`. DESIGN-07 pins the break site: `getUser()` does
> `TIERS.includes(id) ? id : 'owner'`, so once `id` is a person that test is false and
> **every user falls through to `owner`**.
>
> **Decision to make: what renders before `/current-user` resolves.** Rendering the shell
> against a not-yet-known permission set flashes controls off then on. Recommend
> blocking: one round-trip on an internal tool, and it avoids showing controls the user
> may not have.
>
> Two options:

What came out, and why each was safe:
- *exactly right* (E3) - rating the source; "pins the break site" already credits it.
- The whole *display bug rather than a data-loss bug* sentence (E2) - answers an objection
  nobody made. The severity claim it defends was never disputed.
- *blocking on a splash costs a gate we don't have today* (E1) - arguing the rejected
  option's merits after recommending the other one.
- *viable ... pick one when building* (E1) - narrating that a choice is a choice.

What stayed, deliberately: the `TIERS.includes(id) ? id : 'owner'` mechanism, the
consequence (*every user falls through to `owner`*), and the reason for the
recommendation (*one round-trip*). Those are the guard and the consequence from the
`false-positives.md` technical keep-column - cutting them would remove the point of the
paragraph.

---

## 6. A cluster that should be LEFT ALONE

Not every trip through the catalog is a finding. This human paragraph trips *several*
patterns and is still fine:

> Honestly, I don't know. The report is high quality but the methodology bugs me, and
> I've read it three times now - once on the train, once at 2am, once out loud to my
> cat - and I still can't tell if the sample was biased.

It has "honestly", an em dash, a rule-of-three, a hyphenated pair. But it also has
mixed feelings, hyper-specific detail (2am, the cat), and varied rhythm - the human
signals in `false-positives.md`. The tells are incidental, not clustered around
inflation or promotion. **Do not flag it.** This is the calibration target: the skill
should recognize this as a person writing.
