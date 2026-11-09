# Healthcare Appeal Letter Generator with Public Decision Analytics

## Project Overview

This Django prototype helps a healthcare appeals coordinator prepare an editable appeal letter draft using fictional case information and historical public decision analytics.

The application does not use artificial intelligence or real patient information.

## Data Source

California Department of Managed Health Care (DMHC)  
Independent Medical Review (IMR) Determinations, Trend

Official dataset:
https://data.ca.gov/@california-department-of-managed-health-care/independent-medical-review-imr-determinations-trend

CSV downloaded: November 7, 2026.

The initial import included 42,710 records and skipped 39 duplicate reference IDs.

## Setup

These instructions are for Windows PowerShell.

After cloning or downloading the Capstone repository, open a terminal in the main Capstone folder and navigate to the prototype folder:

```powershell
cd prototype
```

Run the remaining commands from the `prototype` folder.

Create a Python virtual environment:

```powershell
python -m venv .venv
```

Activate the virtual environment:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install the required package:

```powershell
python -m pip install -r requirements.txt
```

Create the SQLite database tables:

```powershell
python manage.py migrate
```

Download the official CSV dataset and save it as:

`data/dmhc_imr.csv`

Create the `data` folder inside `prototype` if it does not already exist.

Import the public decisions:

```powershell
python scripts/import_dmhc.py
```

Check the Django application:

```powershell
python manage.py check
```

Run the automated tests:

```powershell
python manage.py test draft_analysis
```

Start the application:

```powershell
python manage.py runserver
```

Open http://127.0.0.1:8000/ in a browser.

Press `Ctrl + C` in the terminal to stop the application.

## Application Features

The application includes:

- A treatment category dropdown populated from the SQLite database.
- A review type dropdown populated from the SQLite database.
- Fields for fictional denial information, medical necessity explanation, and supporting documents.
- Historical decision statistics filtered by both treatment category and review type.
- Counts of total decisions, upheld decisions, and overturned decisions.
- Three example source reference IDs from the matching DMHC records.
- An editable, template-based healthcare appeal letter draft.

## Data Quality and Analytics

The import script checks for missing required values, duplicate reference IDs, and invalid report years.

The application counts historical decisions by treatment category, including decisions that upheld or overturned the health plan's determination.

The application also filters decisions by review type and displays three example source reference IDs from the matching records.

Using the November 7, 2026 dataset, Pharmacy and Medical Necessity returned:

- Total decisions: 10,646
- Health plan decisions upheld: 4,071
- Health plan decisions overturned: 6,575
- Example source reference IDs: MN01-594, MN01-606, MN01-607

The three reference IDs are examples of matching records, not a complete list of the records included in the statistics.

These historical statistics do not predict the outcome of an individual appeal.

## Automated Testing

The application includes four automated Django tests:

1. Required fields cannot be left blank.
2. Denial reasons exceeding 100 characters are rejected.
3. Invalid treatment categories are rejected.
4. Historical statistics and source reference IDs are correctly filtered by treatment category and review type.

All four tests passed on November 8, 2026.

The statistics test uses fictional decision records in a temporary Django test database. The tests do not modify the imported public DMHC records.

## Privacy and Limitations

Use fictional case information only. Do not enter real patient information.

Generated letters are drafts for coordinator review and editing. They are not automatically submitted to health plans.

The local database, downloaded CSV, and Python virtual environment are excluded from Git.

The application does not automatically detect or remove patient identifiers entered by a user. It is a local educational prototype, not a production healthcare system.