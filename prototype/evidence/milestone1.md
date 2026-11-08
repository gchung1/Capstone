
# Milestone 1 — Working Prototype and Public Data Integration

**Course:** CIDM 6395 — Fall 2026  
**Project:** Healthcare Appeal Letter Generator with Public Decision Analytics  
**Evidence recorded:** November 7, 2026  
**Milestone target:** November 8, 2026

## 1. Working Django Prototype

The Django application was created using Python 3.13 and Django 5.2.19.

The application successfully:
- Displays a form for fictional healthcare appeal information.
- Validates the required input fields.
- Retrieves historical decision counts from SQLite.
- Generates an editable appeal-letter draft containing the case information and historical statistics.

The Django system check completed successfully:

    System check identified no issues (0 silenced).

Screenshot: `working-prototype.png`

## 2. Official Public Data Source

**Publisher:** California Department of Managed Health Care (DMHC)

**Dataset:** Independent Medical Review (IMR) Determinations, Trend

**Source:** https://data.ca.gov/@california-department-of-managed-health-care/independent-medical-review-imr-determinations-trend

**Downloaded:** November 7, 2026

The original CSV is excluded from Git. The import script allows the database to be recreated from the downloaded CSV.

## 3. SQLite Data Import Results

Import script: `scripts/import_dmhc.py`

| Check | Result |
|---|---:|
| Records imported | 42,710 |
| Duplicate reference IDs skipped | 39 |
| Records skipped for missing required values | 0 |
| Records skipped for invalid years | 0 |
| Distinct treatment categories | 58 |
| Health plan decisions upheld | 20,279 |
| Health plan decisions overturned | 22,431 |

The import uses five fields: ReferenceID, ReportYear, TreatmentCategory, Type, and Determination.

## 4. Tested Analytics Query

**Treatment category:** Pharmacy

| Outcome | Count |
|---|---:|
| Total decisions | 11,936 |
| Health plan decisions upheld | 4,736 |
| Health plan decisions overturned | 7,200 |

These counts were verified through a Django database query and displayed successfully on the webpage.

## 5. Privacy and Limitations

The form is intended for fictional cases only. No real patient information is required.

Historical DMHC independent medical review decisions provide public data context; they do not predict the outcome of an individual appeal.

Generated letters are editable drafts for coordinator review, not automatically submitted appeals.

## 6. Reproducibility

The project includes:
- `requirements.txt` for Python dependencies.
- `manage.py` and Django application code.
- Database migration files.
- `scripts/import_dmhc.py` to recreate the imported decision records.
- `README.md` with setup instructions.

The virtual environment, downloaded CSV, and local SQLite database are excluded from Git.
