# Diotima White Paper — Reviewer Feedback

## Overview

The white paper has been reviewed across two rounds. Six reviewers received v1 in March 2026; two additional reviewers provided feedback on v2 in April 2026. All reviewers were positive overall.

---

## V1 Reviewers (March 2026)

### Declan McKibben — ADAPT

- Paper reads more marketing than academic
- "erodes" professional judgment: too strong, needs citation or softening
- "implications not absorbed": unsupported market claim, needs evidence or softening
- "do their job better": vague, needs precision
- "Explainability is not a single mode": unclear phrasing
- Questioned whether rejection reason analysis is automated or just manual/human review
- **Overall:** excellent defence of safe/compliant AI in education

**Status:** All comments addressed in v2.

---

### Shunyu Ji — ADAPT

- Central question and answer of paper clearly identified
- Wants a table mapping lifecycle stages to governance dimensions
- Section titles are inconsistent in register across the 6 architectural sections
- Each section should follow consistent structure: regulation → design principle → lifecycle stage
- Most sections don't cite specific EU AI Act articles (only Human Oversight cites Art. 14)
- Introduction says 11 sections; paper actually has 12 — section count error

**Status:** All comments addressed in v2. Structural consistency point further addressed in v2.1 (converged with Ian O'Keeffe's independent feedback).

---

### Ashish Kumar Jha — Trinity Business School / ADAPT

- Very positive ("brilliantly written"), technical sections land well and "come across as fair"
- One minor note: Section 2 reads as extension of intro; should identify 2–3 core challenges that Section 3 then answers directly

**Status:** Addressed in v2.

---

### Gary White — NTA

- Very strong overall, sections on oversight/grounding/explainability/monitoring particularly strong
- Promotional tone toward the end risks undermining credibility of the rigorous sections
- Suggests clean separation: white paper as purely analytical/informative; promotional materials come later
- Recommends reaching out to Dept of Education (knows they are looking for solutions in this space)

**Status:** Promotional tone addressed in v2. Dept of Education outreach noted as action item.

---

### Declan Sheehan — NTA

- Excellent, pitched perfectly, narrative clear, nothing underdeveloped
- Only note: expand acronyms for non-specialist readers (DPIA, benchmark names)

**Status:** Addressed in v2.

---

### Jonathan Dempsey — Diotima Founder

- Word "moat" signals investment/market-positioning over purpose-driven values — prefers framing compliance as "the floor we build on"
- Was going to suggest genericising away from secondary schools for investability but dropped it (document is true to what's been built)
- Academic/industry split observation: academics say too marketing; industry says pitch perfect

**Status:** "Moat" framing removed in v2. Academic/industry tension informed the tone calibration throughout.

---

## V2 Reviewers (April 2026)

### Long Long Thanh Mai — Chief Data Scientist, Diotima (TCD)

- All architecture descriptions confirmed as correct
- One change requested: replace "custom safety evaluations targeting educational contexts" with SimpleSafetyTests (Vidgen et al., 2023) in Model Governance section

**Status:** Incorporated in v2 (commit 0ef1319). Vidgen et al. 2023 added to references.

---

### Ian O'Keeffe (okeeffi / Guest)

25 annotations extracted from annotated PDF. Two accounts used ("okeeffi" and "Guest") — believed to be the same reviewer.

#### Structural comments

- **Design responses too Diotima-specific** — missing generalised principles that readers can apply to their own context. Suggests splitting "Design response" into a general principle followed by Diotima-specific implementation.
- **Sections 5–10 confusing** — needs an overarching heading with an intro explaining the consistent three-part structure (regulatory obligation, design response, lifecycle coverage).
- **Diotima as case study** — should be stated explicitly; the principles are more broadly applicable than the paper currently conveys.
- **Title too narrow** — "Formative Assessment" in the title limits broader applicability. The governance principles aren't inherently tied to formative assessment.

#### Specific comments

- **"Annex III"** — could there be a less technical way to refer to it for a wider readership?
- **"educational AI platform"** — reader might take a narrow interpretation vs broader "AI-enabled" tool
- **"workflow property"** — jargon; suggests "human-centric architecture" or "human intelligence layer"
- **"Section 12 concludes"** — needs more of a teaser to make the reader want to get to the end
- **LLM outputs described too negatively** — "no inherent connection to the curriculum" reads as if outputs are always wrong
- **"content"** — loaded term in educational context; could be confused with "learning content" vs AI-generated output
- **Bloom's Taxonomy** — second citation redundant; let the citation do the work without forcing unfamiliar readers to parse the term
- **AI pre-check (step 3)** — unclear whether this is student-facing or teacher-centric
- **Step 4 vs step 3** — unclear distinction between conditional rubric visibility and the pre-check
- **Step 5 (teacher confirmation)** — undersells that teachers can edit/augment/enhance, not just confirm
- **Curriculum grounding and complexity** — alignment at age-appropriate complexity level should be called out, not just curriculum content
- **Second Bloom's citation** — redundant
- **High-risk perimeter** — questions whether this is aspirational or how things actually are; notes the concept deserves its own paper
- **"natural persons"** — legal terminology, could be phrased more accessibly
- **"teacher-confirmed results"** — "results" might be confused with scores/grades in educational context
- **"AI's reasoning context"** — unclear what this includes beyond source text; is the system prompt shared?
- **Rejection feedback loop** — referenced before it's introduced to the reader
- **BESA/UK compliance gap** — needs citeable sources
- **"considering AI-assisted formative assessment"** — questions how much this is tied to formative assessment specifically vs education in general

**Status:** All actionable comments addressed across v2.1 and v2.2:
- v2.1: Governance sections restructured (parent section + 6 subsections, each with general principle + Diotima implementation)
- v2.2: Case study framing in intro, DfE citation added, 11 clarity edits (workflow property, natural persons, steps 3–5, LLM description, Bloom's citation, conclusion teaser, reasoning context, feedback loop forward-reference)
- Not changed: title (strategically correct to keep "Formative Assessment"), "Annex III" terminology (paper's audience requires regulatory precision)

---

## Summary of versions

| Version | Tag | Key changes |
|---------|-----|-------------|
| v1 | `v1` | Original journal-style paper |
| v2 | `v2` | All v1 reviewer feedback incorporated |
| v2.1 | `v2.1` | Governance sections restructured with general principles |
| v2.2 | `v2.2` | Case study framing, BESA/DfE citation, clarity edits |
