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

## 5. A cluster that should be LEFT ALONE

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
