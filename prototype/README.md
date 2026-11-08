
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

## Setup

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

Import the public decisions:

```powershell
python scripts/import_dmhc.py
```

Start the application:

```powershell
python manage.py runserver
```

Open http://127.0.0.1:8000/ in a browser.

## Data Quality and Analytics

The import script checks for missing required values, duplicate reference IDs, and invalid report years.

The application counts historical decisions by treatment category, including decisions that upheld or overturned the health plan's determination.

These historical statistics do not predict the outcome of an individual appeal.

## Privacy and Limitations

Use fictional case information only. Do not enter real patient information.

Generated letters are drafts for coordinator review and editing. They are not automatically submitted to health plans.

The local database, downloaded CSV, and Python virtual environment are excluded from Git.
