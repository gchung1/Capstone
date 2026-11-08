# ADR-004: Provide Copy-Paste and PDF Download Options

Date: 2025-11-14
Status: Accepted

Context

- Problem/forces:
  - Users may want to copy letters directly or download as PDF.
  - Simple UI required for beginners.
 

Decision

- Display generated letter in a textarea and provide a "Download PDF" link.
  - Gives users flexibility to copy/paste or download.
  - Simple to implement using Django and ReportLab.

Consequences

- Positive:
  - Beginner-friendly interface.
  - Supports multiple use cases.
- Negative/Risks:
  - Extra step in backend for PDF generation.

Validation

- Measure:
  - User can copy letter from textarea.
  - User can click link to download PDF with the correct content.
- Rollback:
  - Could remove PDF if PDF generation causes errors.
