# Consultation Response to Proposal Feedback

## 1. Who uses the prototype, and what action do they take?

One healthcare appeals coordinator employed by a provider uses the application. The coordinator selects the denied service category and review basis, supplies fictional case details and supporting document information, then reviews and copies a letter draft incorporating a clearly labeled summary of comparable public IMR decisions. A professional reviews the letter before any real world use. The prototype never decides coverage, sends an appeal, or accepts actual patient records.

## 2. Which real public records will be used, and how do they meet the data conditions?

Original publisher: California Department of Managed Health Care (DMHC), _Independent Medical Review (IMR) Determinations, Trend_.  

Agency publication page: https://data.ca.gov/@california-department-of-managed-health-care/independent-medical-review-imr-determinations-trend  

Official publishing catalog: https://publish.data.ca.gov/dataset/independent-medical-review-imr-determinations-trend  

Source metadata inspected: October 28, 2026.

Records not yet imported. The first actual retrieval date will be entered in `Capstone/prototype/README.md` and logged. 

Four relevant checks:

1. Relevance: The DMHC dataset contains actual independent medical review decisions involving denied, delayed, or modified healthcare services. Fields such as treatment category, review type, and determination directly support the coordinator's search and the historical analysis included in the appeal letter.

2. Accountability: The California Department of Managed Health Care is the original government publisher responsible for the data. The dataset is publicly available under a Creative Commons Attribution license. The prototype README will document the agency, official source URL, actual retrieval date, selected fields, and any changes made during preparation.

3. Availability: The records are available now through California's official open data portal as a CSV file, accompanied by a data dictionary. A Python script will retrieve the records directly from the government source and load a manageable subset into SQLite. The script and instructions will be included in the repository so the professor can reproduce the process without special permission.

4. Quality: The dataset contains individual decisions spanning multiple years, treatment categories, and outcomes. This provides real transactional variety for analysis. Before using the records, Python will check for missing values, duplicate identifiers, inconsistent categories, and unexpected values. Any corrections, exclusions, and resulting record counts will be documented. I will verify these characteristics during import rather than assume particular data problems exist.

The prototype will analyze real public DMHC decisions, not invented appeal records. Only the coordinator's example case details will be fictional. Historical decisions will provide context for the letter but will not predict the outcome of an individual appeal.

## 3. Trace one source record to the screen. How does analysis change the letter?

The state's public dataset preview shows ReferenceID: MN26-46986, ReportYear: 2026, TreatmentCategory: Pharmacy, Type: Medical Necessity, and Determination: Overturned Decision of Health Plan. This is a specific published example to verify against the live source during import. No aggregate totals are claimed yet.

Planned trace: agency row MN26-46986 → importer checks and stores the columns in SQLite → the coordinator selects Pharmacy / Medical Necessity → a parameterized query returns matching public rows → Python counts total, upheld, and overturned decisions → Django displays the counts and source reference IDs → the letter template inserts the actual computed counts in a labeled historical context paragraph. If the selected category changes, that paragraph changes as well. The factual results are context, not a medical necessity finding or a predicted appeal outcome.

## 4. Which language model API is proposed, and what happens without a key?

No language model API will be called in this term's prototype. Appeal letter drafts will be generated locally using a Python template, fictional case details, and statistics calculated from real public DMHC records.

This approach requires no API key, subscription, or paid service. The professor can run the complete prototype without an OpenAI account. The OpenAI Responses API may be considered as a future enhancement to the full project, subject to approval, but it is not part of the current prototype. No real patient information will be entered or sent to an external AI service.

## 5. What file proves that the first milestone is complete?

`Capstone/prototype/evidence/milestone1.md` will document the milestone by November 8, 2026. It will contain the exact setup/import commands, a successful `python manage.py check` result, a recorded row count after importing the official DMHC subset, a sample category query, and a reference to a screenshot of the running form. The companion `Capstone/prototype/README.md` will document the agency URL, the actual import date, selected fields, and reproduction instructions. These are future evidence files and not yet completed results.

## Additional required corrections

- The revised diagram is a one-way flow corresponding to Section 2 of the proposal with a security validation gate before data processing and a single letter output.
- The portfolio links now point to `Capstone/portfolio/{BA,DM,SS,CN}/README.md`.
- The `feedback/` folder is retained.
- Django secret key remediation was completed on October 29, 2026. The exposed key was replaced with a reference to the `DJANGO_SECRET_KEY` environment variable in `settings.py`. A new random key was generated and stored outside the repository. Testing confirmed that the settings file successfully loads the new key. The previously exposed key remains in Git history and will not be reused.
