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

## November 23, 2026 — Capstone Revisions per Debrief Feedback

### DMHC Treatment Category Data Quality

- **Task and output:** Used ChatGPT to review existing `import_dmhc.py`, `models.py`, and `forms.py` files. ChatGPT suggested simple code changes to standardize confirmed equivalent treatment category labels and later add a basic check for possible capitalization and spacing inconsistencies.

- **Kept or changed:** Updated `prototype/scripts/import_dmhc.py` to standardize `Gen Surg proc` as `Gen Surg Proc` and `DME` as `Durable Med Equip`. Retained `DME MACs` as a separate category. Added an import counter and a report of possible category-label inconsistencies without automatically changing uncertain labels. The original database model and form structure were not changed.

- **Verification:** Ran the Python syntax check and reimported the CSV. The script examined 42,749 rows, imported 42,710 records, skipped 39 duplicate reference IDs, and reported 2,681 normalized category labels. Confirmed that the database and webpage dropdown showed `Gen Surg Proc` and `Durable Med Equip` without separate `Gen Surg proc` or `DME` entries. The later consistency check identified `Admin Misc  Invest` as having extra spaces; it was reported but left unchanged. Created a local SQLite database backup before the initial reimport.

### Report Year Filter and Historical Analytics

- **Task and output:** Used ChatGPT to review existing Django view and HTML template and suggest a basic year dropdown code in response to feedback that the historical counts combined all available report years.

- **Kept or changed:** Updated `prototype/draft_analysis/views.py` and `prototype/draft_analysis/templates/draft_analysis/home.html` to add an optional Report Year selection with `All Years` as the default. The selected year filters the historical decision counts and is included in the generated letter's Public Decision Data Context. Retained the existing treatment category, review type, and appeal letter workflow.

- **Verification:** Tested the application in the browser with fictional information. Confirmed that the selected year appeared in the historical analysis and that `for 2025` appeared in the generated letter's Public Decision Data Context.

### Automated Test Improvements

- **Task and output:** Used ChatGPT to code additional tests for an invalid category test used an empty test database. ChatGPT also suggested testing the new year filter.

- **Kept or changed:** Updated `prototype/draft_analysis/tests.py` to create known valid test choices, verify that a valid treatment category is accepted, check required fields with valid selections, and verify that choosing a year limits the returned statistics. Retained the original testing purposes and used fictional records in Django's test database.

- **Verification:** Ran `python manage.py test draft_analysis` after the year filter and test updates. All seven tests passed with no Django system-check issues. The tests have not yet been rerun after the final category-inconsistency reporting change.

### README and Portfolio Evidence Corrections

- **Task and output:** Used ChatGPT to review my README, competency inventory, and Systems Development appraisal against the professor's feedback and for formatting/spelling/grammar.

- **Kept or changed:** Updated `prototype/README.md` with `source .venv/bin/activate`, documentation of the year filter and category normalization, and the seven automated tests. Updated only the CIDM 6351 row in `portfolio/inventory/README.md` and removed the unsupported Python, Jupyter Notebook, and JSON sentence from `portfolio/SS/README.md`. Kept the remaining course entries, existing evidence links, appraisal structure, and overall wording as close to the originals as possible.

- **Verification:** Reviewed and saved the documents in VS Code. Confirmed with `git status --short` that the updated README and portfolio files were detected as modified. The macOS/Linux instructions were documented but not tested on those operating systems.

### Synthesis Paper Revisions

- **Task and output:** Used ChatGPT to review revised synthesis paper for formatting, spelling, grammar, and alignment with feedback.

- **Kept or changed:** Added repository paths for coursework artifacts and curricular appraisals, briefly documented the year filter and category standardization, updated the test discussion from four original tests to seven current tests, and added a short one year learning plan for Python, database development, Django architecture/testing, and cybersecurity implementation. Preserved the existing introduction, personal reflections, scope decisions, and overall paper structure. Replaced the local `deliverables/synthesis-paper.pdf` with the revised version.

- **Verification:** Reviewed the proposed changes and replaced the PDF in the Capstone folder. Confirmed that Git listed `deliverables/synthesis-paper.pdf` as modified. The revised paper has not yet been included in a consolidated commit.