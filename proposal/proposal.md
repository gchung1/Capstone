# Capstone Project Proposal

## Healthcare Appeal Letter Drafting Assistant with Public Decision Analytics

### 1. Pretext

A healthcare appeals coordinator at a provider organization needs to draft letters after denied treatment requests. On one local webpage, the coordinator enters fictional case details and receives an editable letter informed by real public independent medical review (IMR) decisions. The coordinator reviews and copies the draft. The application neither submits appeals nor provides medical advice.

### 2. Process Flow

![One connected workflow across the four capstone areas](diagram.png)

**SS** collects the category, denial basis, and fictional details in Django. **CN** validates entries and protects secrets. **DM** retrieves public DMHC decisions from SQLite. **BA** counts matching, upheld, and overturned decisions. **SS** inserts those findings into a letter for coordinator review. Without SS there is no interface, CN no validation, DM no source records, or BA no computed context.

### 3. Synthesis Prototype

The minimum demo has one Django form, SQLite table, category query, and editable letter. Python validates entries and inserts three calculated counts into a historical context paragraph that changes with the selected category. No dashboard, accounts, cloud hosting, or real patient data are included.

### 4. Full Project

A one year expansion could add authorized data, accounts, and cloud hosting. DM would govern records, BA analyze them, SS run the interface, and CN enforce privacy and access. These additions are outside this term's prototype.

### 5. Data

| Source | Authority | Grain | Access | Terms |
|---|---|---|---|---|
| [IMR Determinations, Trend](https://data.ca.gov/@california-department-of-managed-health-care/independent-medical-review-imr-determinations-trend) | California DMHC | One IMR decision | Public CSV bulk file | Creative Commons Attribution (CC BY) |

**Relevance:** Treatment, review type, and outcomes inform the letter. **Accountability:** The California Department of Managed Health Care (DMHC) publishes the data; the README will record its URL, terms, retrieval date, fields, and transformations.

**Availability:** The public CSV and dictionary are retrievable by `Capstone/prototype/scripts/import_dmhc.py`. **Quality:** Decisions span years and categories; Python will check missing data, duplicates, and inconsistent values and log cleaning.

**Synthetic data:** None in the analysis; fictional form inputs are demonstration-only, so synthetic-data conditions do not apply.

### 6. Tools and Platform

Python, Django, SQLite, and HTML run locally. A Python template drafts letters without a language-model API, key, or fee. The OpenAI Responses API is deferred pending approval. Django loads its secret from an environment variable. Case inputs are fictional.

### 7. Risks and First Milestone

Time, data changes, and privacy risks are managed through narrow scope, documented imports, and validation. By November 8, 2026, the form, SQLite import, and category query will work. `Capstone/prototype/evidence/milestone1.md` will record commands, results, counts, and a screenshot reference.

### 8. Evidence I Build On

Portfolio evidence: `Capstone/portfolio/BA/README.md`, `Capstone/portfolio/DM/README.md`, `Capstone/portfolio/SS/README.md`, and `Capstone/portfolio/CN/README.md`. My prior HealthAppeals work supports Django development; this prototype joins all four areas in one path.

### 9. AI Use

Help interpret code, troubleshoot, and review writing. The default letter draft uses a transparent Python template.
