# AI Use Log

**Project:** Healthcare Appeal Letter Generator with Public Decision Analytics

## AI Tool and General Use

**Tool:** OpenAI ChatGPT  
**Model:** GPT-6

This capstone was developed from my own project idea and decisions about its purpose, features, and overall direction. My initial coding knowledge and code ideas were basic, thus I used ChatGPT to cross check my approach, improve code, troubleshoot problems, and help turn my ideas into a working application.

ChatGPT also provided code examples and documentation drafts that I reviewed and tested prior to accepting. In general, AI was and will be used to check formatting and grammar/spellcheck for all documents I drafted for consistency. Additionally, AI was and will be used to help keep project organized per requirements and deadlines.

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