# AI Use Log

**Project:** Healthcare Appeal Letter Generator with Public Decision Analytics

## AI Tool and General Use

**Tool:** OpenAI ChatGPT  
**Model:** GPT-6

This capstone was developed from my own project idea and decisions about its purpose, features, and overall direction. My initial coding knowledge and code ideas were basic, thus I used ChatGPT to cross check my approach, improve code, troubleshoot problems, and help turn my ideas into a working application.

ChatGPT also provided code examples and documentation drafts that I reviewed and tested prior to accepting. In general, AI was and will be used to check formatting and grammar/spellcheck for all documents I drafted for consistency. Additionally, AI was and will be used to help keep project organized per requirements and deadlines. Additionally, it was and will be used to maintain AI use and task log here.

## November 7, 2026 — Prototype/Milestone Development

### Project Setup and Web Form

- **Task and output:** Reviewed my approach and provided Django setup commands for the application, input form, and webpage accordingly based on basic code provided.
- **Kept or changed:** Used and adjusted the code to fit my project idea, chose the application name `draft_analysis`, revised the page title, and relocated the disclaimer.
- **Verification:** Ran Django's system check and successfully submitted fictional information through the form.

### Data Import and Analytics

- **Task and output:** Troubleshoot and improve basic code for the SQLite database model, CSV import script, and queries using official California DMHC data.
- **Kept or changed:** Selected five relevant dataset columns and used the suggested code to import and analyze the records.
- **Verification:** Imported 42,710 records, identified 39 duplicate IDs, and verified the Pharmacy results: 11,936 total decisions, 4,736 upheld, and 7,200 overturned.

### Appeal Letter Generator

- **Task and output:** Troubleshoot and improve basic code for letter drafting concept into Python and HTML code that combines fictional appeal information with historical statistics.
- **Kept or changed:** Kept the generator simple, editable, and template based without adding paid AI services.
- **Verification:** Troubleshot a missing HTML section and confirmed that the generated letter appeared and could be edited.

### Security and Documentation

- **Task and output:** Reviewed code and provided suggestions for protecting project files, correcting Django settings, general editing of the README and milestone evidence, and documenting AI use, and grammar, spelling, and consistent formatting per requirements.
- **Kept or changed:** Removed the duplicate hardcoded secret key and excluded the local database, CSV, and virtual environment from Git.
- **Verification:** Confirmed Git exclusions using `git check-ignore` and ran Django's system check successfully.

### Portfolio Feedback and Documentation Corrections

- **Task and output:**  Review and organize the professor's November 7 feedback including checking my corrections and formatting to Snowflake and PostgreSQL descriptions, outdated synthetic data references, and repository file paths.

- **Kept or changed:** Updated the BA, DM, SS, CN, and skills inventory documents to accurately reflect my PostgreSQL coursework, real California DMHC data, and template based letter generator. Corrected artifact links in the BA portfolio and outdated folder paths in the proposal documents.

- **Verification:**  Reviewed and saved the changes in VS Code, checked the modified files using git status --short, and ran git diff --check without errors. Used git grep to confirm the old folder paths were no longer present in the checked documents.

## November 8, 2026 — Prototype Improvements

### Treatment Category Dropdown and Testing

- **Task and output:** Used ChatGPT to help review the existing Django form and views, replace the free text treatment category with a dropdown populated from the SQLite database, and run appropriate tests to test various scenarios.

- **Kept or changed:** Updated forms.py to use Django's ChoiceField and retrieve valid treatment categories from the DMHC records. Kept the remaining form fields and existing letter generator unchanged.

- **Verification:** Ran python .\prototype\manage.py check successfully. Tested the application in the browser with fictional information. Pharmacy returned 11,936 total decisions, 4,736 upheld, and 7,200 overturned. Surgery returned 83 total decisions, 33 upheld, and 50 overturned. Confirmed that changing the selected category changed the displayed statistics and letter generator content accordingly.

### Review Type Dropdown and Double Filter Data Analysis

- **Task and output:** Used ChatGPT to draft code to add a Review Type dropdown and update the Django database query to filter historical DMHC decisions by both treatment category and review type.

- **Kept or changed:** Updated `forms.py` to retrieve valid review types from SQLite, `views.py` to use both selections when calculating statistics, and `home.html` to display the selected review type. Updated the generated letter to explain which records were included.

- **Verification:** Ran Django's system check without errors. Tested Pharmacy with Medical Necessity in the browser and obtained 10,646 total decisions, 4,071 upheld, and 6,575 overturned. Independently verified all three counts using a direct Django database query. Confirmed that the webpage and editable letter displayed the correct selections and statistics.

### DMHC Source Reference IDs

- **Task and output:** ChatGPT was used to help correct drafted code to display source reference IDs from the real California DMHC records used in the historical analysis.

- **Kept or changed:** Corrected code. Updated views.py to retrieve three reference IDs matching the selected treatment category and review type. Updated home.html to display those IDs alongside the calculated statistics.

- **Verification:** Ran a direct Django database query that returned MN01-594, MN01-606, and MN01-607 for Pharmacy and Medical Necessity. Tested the webpage and confirmed that the three IDs appeared correctly. Verified that the historical counts remained 10,646 total, 4,071 upheld, and 6,575 overturned, and that the editable letter still generated successfully.