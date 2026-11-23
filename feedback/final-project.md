# Final Capstone Feedback

Gina,

I reviewed your repository at commit `ad453a0`, your last commit, of November 13. I read the paper, the slides, and the portfolio, watched the video, and ran the prototype from a new clone by the steps in `prototype/README.md`. The download script retrieved the DMHC file, the import loaded 42,710 records, and the four tests passed. Pharmacy with Medical Necessity gave 10,646 decisions, 4,071 upheld and 6,575 overturned, with the same three reference IDs as in your paper. I reproduced every figure you report.

## Reviewed artifacts

- Portfolio: `README.md`, `portfolio/BIO.md`, `portfolio/inventory/README.md`, and `portfolio/BA`, `DM`, `SS`, and `CN`, each with its `README.md` and the work it cites.
- Prototype: `prototype/`, with `scripts/download_dmhc.py`, `scripts/import_dmhc.py`, `draft_analysis/`, and `evidence/`.
- Paper: `deliverables/synthesis-paper.pdf`, seven pages.
- Slides: `deliverables/slides.pptx`, eight slides.
- Video: `deliverables/video.mp4`, 11 minutes 24 seconds.
- AI use: `AI_LOG.md` and the AI Use section of the root README.

Every required file is at its required path, with one exception. The script that retrieves the data is in `prototype/scripts/`, not in `prototype/data/`. Your README says where it is, so I found it at once.

## What is strong

The prototype does what the approved proposal says it will do. A coordinator selects a treatment category and a review type, enters a fictional case, and receives counts from real California decisions together with a letter draft that the coordinator can edit. The data move from the CSV to SQLite, then to the counts, then into the letter, so the prototype does not run if you remove any one of data management, analytics, or systems development.

The change of data was the best decision in the project. Your first proposal used synthetic denial records. The final version uses the determinations that the DMHC publishes, retrieved by a script that I ran without any change. The paper explains this choice, and it explains the choice of SQLite and of a fixed template in place of a language model.

`AI_LOG.md` records, for each use of ChatGPT, the task, what you kept or changed, and how you verified the result. In the November 8 entry you checked the three counts with a direct database query, so you did not take the code's output on trust.

The paper and the video are clearly your own project. Your healthcare and insurance experience defines the problem, and you set the scope and its limits candidly: fictional cases only, no prediction, and no submission to a plan.

You made each fix that the evolution addenda asked for. The Snowflake claims now agree with your PostgreSQL sample. The HealthAppeals zip has no `.venv` or database. The Data Mining and Management appraisal now describes the DMHC data.

## What needs attention

- Your proposal and your consultation response said that the import would check for inconsistent categories. `import_dmhc.py` checks for missing values, duplicate reference IDs, and invalid years, but it does not check the category labels. The Treatment Category list shows the result: it contains both `Gen Surg Proc` and `Gen Surg proc`, and it lists `DME` next to `Durable Med Equip`.
- The analytics are three counts over all years from 2001 to 2026 together. A filter by year, or a comparison of recent years with earlier years, would give a coordinator more than one total.
- `test_invalid_treatment_category` runs on an empty test database, where every category is invalid. Thus the test cannot fail. Add a test that shows a valid category is accepted.
- The paper refers to your artifacts and your appraisals by title, but it does not cite a file, an appraisal section, or a commit. Your repository holds that evidence, so a reader could check each claim if the paper gave its path.
- The paper lists the weaknesses that the one-year plan depends on (advanced Python, database development, software architecture, and security implementation). It does not say how the year would close them.
- The README gives Windows PowerShell commands only. Add the macOS and Linux activation line.
- The inventory row for CIDM 6351 and line 42 of the Systems Development appraisal still claim Python, Jupyter, and JSON work for that course with no sample.

## Synthesis

The prototype integrates systems development, data management, and data analytics, and networking and cybersecurity sets its limits. The paper treats all four areas and explains why security is a design constraint here and not a component. The slides map each feature to an area. The video does not connect the prototype to your portfolio, your bio, or the paper.

## Debrief themes

Our conversation will cover these areas:

1. Design rationale, including the choice of a template over a language model.
2. Technical implementation, including the code that the AI log says you drafted with assistance.
3. Data quality and what the counts mean for a coordinator.
4. The evidence behind the claims in the paper.
5. The one-year plan, its limits, and professional readiness.

## Most important next step

Reconcile the category labels at import and report the result with counts, as your proposal promised. Until then, a coordinator who selects either `Gen Surg` label receives a count that includes both.

Jeff
