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

### Input Validation and Testing

- **Task and output:** Reviewed the existing Django form validation and help draft automated tests for required fields, character limits, and invalid treatment category selections.

- **Kept or changed:** Kept the existing form validation without adding unnecessary code and tests. Updated `tests.py` to include three automated tests to verify the existing validation rules.

- **Verification:** Ran `python .\prototype\manage.py test draft_analysis` successfully. All three tests passed without errors. Confirmed that Django used a temporary test database without changing the imported DMHC records.

Also, added a fourth automated test using fictional decision records in Django's temporary test database. Verified that the application correctly filters by both treatment category and review type, calculates the expected decision counts, and displays the matching source reference IDs. Ran all four automated tests successfully without errors.

## November 9, 2026 — Public Dataset Reproducibility

### DMHC Full Dataset Download Script

- **Task and output:** Helped draft code and troubleshoot `prototype/scripts/download_dmhc.py` in order for others to retrieve the complete official California DMHC CSV dataset without storing the large file on GitHub.

- **Kept or changed:** Replaced the original Python download method after it received an HTTP 403 error. Updated the script to use `curl`, verify the expected CSV column headings, skip downloading if the file already exists, and remove incomplete downloads if an error occurs. Updated only the dataset download instructions in `prototype/README.md`.

- **Verification:** Confirmed that the script skipped the existing CSV. Tested a complete temporary download of approximately 81.45 MB, verified that the script accepted the CSV headings, and removed the temporary file afterward. Ran `git diff --check` without errors

### Clone Reproducibility Test

- **Task and output:** Used ChatGPT for code guidance and troubleshooting to test whether the capstone could be recreated from a fresh GitHub clone using the documented setup instructions.

- **Kept or changed:** Created a separate temporary copy of the repository for testing. No application code, original database, or original CSV files were changed.

- **Verification:** Successfully cloned the repository, created a new Python virtual environment, installed Django 5.2.19, ran database migrations, downloaded the complete official DMHC CSV, and imported 42,710 records. All four automated Django tests passed. Verified that the application displayed the expected Pharmacy and Medical Necessity statistics (10,646 total, 4,071 upheld, and 6,575 overturned), showed the matching source reference IDs, and generated an editable appeal letter.

## November 10, 2026 — Synthesis Paper and Slides

### Synthesis Paper

- **Task and output:** ChatGPT helped review (spelling/grammar/formatting) and tighten/organize the capstone synthesis paper based on what I had drafted.

- **Kept or changed:** Kept reviewed and approved spelling/grammar/formatting suggestions, and organization/tightening that focused on the four curricular areas, portfolio evidence, prototype feasibility, and future expansion. Finalized the approved version as `deliverables/synthesis-paper.pdf`.

- **Verification:** Reviewed the completed paper. Confirmed that it addresses the professor's synthesis paper requirements and that the PDF is saved in the required `deliverables` folder.

### PowerPoint Presentation

- **Task and output:** ChatGPT help tighten and format the presentation - spelling/grammar and improve the overall visual design from what I had initially drafted.

- **Kept or changed:** Reviewed and customized the slides using Microsoft PowerPoint 2013. Kept the presentation focused on my healthcare background, curricular integration, working prototype, historical DMHC decision data, testing, limitations, and one year vision according to the main topics required and discussed within my synthesis paper.

- **Verification:** Confirmed that the presentation opens in Microsoft PowerPoint 2013 and that the final `slides.pptx` file is saved in the required `deliverables` folder.