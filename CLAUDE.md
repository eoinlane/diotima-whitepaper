# Diotima Whitepaper — Claude Context

## Project
White paper produced by Eoin Lane (Noval Consulting) for Diotima, an EdTech AI startup (founder: Jonathan Dempsey). The paper positions Diotima's compliance-by-design approach to AI in education, grounded in the EU AI Act.

## Working files
- `Diotima_Journal_Style_v2.tex` — **active working file** (v2.2, post all reviewer feedback)
- `Diotima_Journal_Style.tex` — archived v1, do not modify
- `Diotima_White_Paper_Noval_Consulting.tex` — Noval Consulting variant
- PDFs are excluded from git via `.gitignore`; use `git add -f` to force-add if needed

## Paper structure (v2.2)
7 sections. Section 5 ("Governance Dimensions in Practice") contains 6 subsections, each structured as: regulatory obligation → general principle (system-agnostic) → In Diotima → lifecycle coverage. Diotima is explicitly framed as a case study of transferable principles.

## Building
```
/usr/local/texlive/2025/bin/universal-darwin/pdflatex <file>.tex
```
pdflatex is not on PATH — use the full path above.

## Strategic framing
- The white paper is the **credibility/analytical document** — keep it rigorous, not promotional
- A separate case study (planned) is the commercial/BD tool — don't conflate the two
- Compliance-as-foundation framing: "the floor we build on", not a competitive moat
- BESA analyst (early 2026) confirmed no supplier is currently compliant with UK Dept of Education AI standards — strong external validation for Diotima's positioning
- Ireland is a foothold market; UK (80M pop) is the real commercial target

## Key people
- Jonathan Dempsey — Diotima founder
- Eoin Lane — Noval Consulting, author; EU AI Act advisory, research fellow
- Long Long Thanh Mai — Chief Data Scientist, Diotima (TCD, MAILT@tcd.ie)
- Reviewers (v1): Declan McKibben & Shunyu Ji (ADAPT), Ashish Kumar Jha (Trinity Business School), Gary White & Declan Sheehan (NTA)
- Reviewer (v2): Ian O'Keeffe
- Jamie Cudden — Chief Digital Officer, Dublin City Council (active client)
