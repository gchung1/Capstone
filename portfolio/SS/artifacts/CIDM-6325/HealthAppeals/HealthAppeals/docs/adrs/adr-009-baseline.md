# ADR-009: Implement Baseline Features for AI Appeal Letter Generator

**Date:** 2025-11-19  
**Status:** Accepted

## Context

- Problem/forces:
  - Project requires a working MVP with baseline functionality before adding advanced features.
  - Users need to generate appeal letters quickly without creating accounts or storing personal data.
  - Admins need a simple interface to manage templates.


## Decision

- Implement baseline features using current Django setup:
  - Form page to collect denial information.
  - Function-based view (FBV) `generate_letter` to generate letters using either a template or AI service.
  - PDF download functionality via `download_pdf`.
  - Admin interface for template CRUD.
  - Display AI and privacy disclaimers.
  - Minimal JavaScript/HTML for mobile-friendly layout.
  - Implemented **form-based input** with `apps.appeals.forms`.
  - `generate_letter` FBV handles AI/template logic and returns rendered letter.
  - PDF download handled via `download_pdf`.
  - Admin interface allows adding, editing, and deleting templates (`apps.appeals.models.Template`).
  - Keep code beginner-friendly, avoiding over-engineering or complex CBVs for this MVP.

## Consequences

- **Positive:**
  - Fully functional MVP that satisfies PRD requirements.
  - Users can generate letters in under 5 minutes.
  - Admins can maintain templates without code changes.
  - Mobile-friendly and privacy-focused.
  - Provides foundation for future features (analytics, multi-language support, advanced AI prompts).
- **Negative/Risks:**
  - Basic AI integration may produce inaccurate letters; users must review before sending.
  - No account system; all usage is anonymous and ephemeral.
  - PDF generation and AI calls may increase server load if usage grows.

## Validation

- **Measure:**
  - Submit form and successfully generate letter.
  - Generated letter can be edited and downloaded as PDF.
  - Admin can create, edit, and delete templates.
  - AI disclaimer visible with every generated letter.
  - Privacy disclaimer visible on the form page.
- **Rollback:**
  - Remove AI integration and revert to static template rendering if issues arise.
  - Disable PDF download temporarily if server load becomes problematic.
