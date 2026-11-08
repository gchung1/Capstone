# ADR-001: Django for the Health Appeal Generator Project

Date: 2025-11-14
Status: Accepted

Context

- Problem/forces:
  - A web-based tool for generating insurance appeal letters needed.
  - Python familiarity.

Decision

- Python
  - Provides built-in support for forms, models, and templates.
  - Has a simple routing system and beginner-friendly documentation.
  - Allows us to quickly integrate AI features and PDF generation.

Consequences

- Positive:
  - Faster development using Django’s conventions.
  - Easier integration with Python libraries like OpenAI and ReportLab.
- Negative/Risks:
  - Slightly more overhead than Flask for a small project.
  - Students must understand Django’s project structure.

Validation

- Measure:
  - The Django project runs locally.
  - Users can navigate to forms and submit requests.
- Rollback:
  - Could switch to Flask if Django proves too complex.
