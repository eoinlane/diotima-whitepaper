# Diotima Whitepaper — Claude Context

## Project
White paper produced by Eoin Lane (Noval Consulting) for Diotima, an EdTech AI startup (founder: Jonathan Dempsey). The paper positions Diotima's compliance-by-design approach to AI in education, grounded in the EU AI Act.

## Working files
- `Diotima_Journal_Style_v2.tex` — **active working file** (v2.4, post Prag Sharma edits)
- `Diotima_Journal_Style.tex` — archived v1, do not modify
- `Diotima_White_Paper_Noval_Consulting.tex` — Noval Consulting variant
- PDFs are excluded from git via `.gitignore`; use `git add -f` to force-add if needed

## Paper structure (v2.4)
7 sections. Section 5 ("Governance Dimensions in Practice") contains 6 subsections, each structured as: regulatory obligation → general principle (system-agnostic) → In Diotima → lifecycle coverage. Diotima is explicitly framed as a case study of transferable principles. Conclusion flags a companion paper on operational controls (metrics, review-effort validation, prompt governance, closed-loop model updates).

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
- Operational controls (metrics, audit of review effort, prompt governance, feedback loops) are deferred to a companion paper — don't conflate with this one

## Launch plan
- **Event:** Diotima Showcase, Thursday 21 May 2026, Trinity College Dublin, 09:45–12:30. Co-hosted by Diotima and Learnovate. White Paper Launch is Eoin's 30-min slot at 10:45. Trials panel chaired by Tom Pollock (Learnovate) with ETBI, Stepaside, Law Society.
- **Learnovate promotional package:** Connections newsletter, press release Mon 25 May (LV8 photographer), white paper published behind a form on the Learnovate site week of 11 May. Final draft lock needed before 11 May.
- **Recommended publication plan (not yet decided):** Learnovate gated PDF primary; Zenodo deposit for a DOI after the gated window (2–4 weeks); ungated mirrors on Noval Consulting and Diotima sites; SSRN optional; skip arXiv.

## Key people
- Jonathan Dempsey — Commercial Lead, Diotima Project, Learnovate Centre, TCD (jonathan@diotima.ai)
- Eoin Lane — Noval Consulting, author; EU AI Act advisory, research fellow
- Long Long Thanh Mai — Chief Data Scientist, Diotima (TCD, MAILT@tcd.ie)
- Reviewers (v1): Declan McKibben & Shunyu Ji (ADAPT), Ashish Kumar Jha (Trinity Business School), Gary White & Declan Sheehan (NTA)
- Reviewers (v2+): Ian O'Keeffe; Mahsa Mahdinejad (Trinity/UL, Diotima postdoc); Donal Geraghty (CEO, Seapark); Prag Sharma (Director of Emerging Technologies, Citi; UCD Smurfit board)
- Tom Pollock — Commercial Development Manager, Learnovate; chairs trials panel at showcase
- Siobhan Ryan — Trinity / Learnovate, co-presents at showcase
- Jamie Cudden — Chief Digital Officer, Dublin City Council (active client)

## Related KB

The pipeline KB at `~/knowledge_base/` holds the conversation history that surrounds the whitepaper / journal. Memory dossier: `~/.claude/projects/-Users-eoin-knowledgebase-pipeline/memory/project_diotima.md` (Diotima covers both the patent/product side and the publication side; sibling sub-project `~/Documents/patents/diotima/` holds the patent track).

GitHub: `eoinlane/diotima-whitepaper` (public). Distinct from `eoinlane/diotima-patent` (private), which holds the invention disclosure and product code.

Top people: Cathal Bellew, Siobhan Ryan, Carl.

Useful queries:

```bash
python3 ~/query_graph.py prep "Siobhan Ryan"                 # Diotima primary
python3 ~/query_graph.py synthesise --project Diotima        # narrative trajectory
python3 ~/query_graph.py tags --search whitepaper            # whitepaper-tagged meetings
python3 ~/query_graph.py history "Cathal Bellew"             # full meeting history
```
