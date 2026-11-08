# ADR-005: Add Basic Admin for Template Management

Date: 2025-11-14
Status: Proposed

## Context

- Problem/forces:
  - The project requirement includes having an admin feature.
  - Needs to be beginner-friendly and simple to manage templates.
  - Users should be able to add/edit/delete letter templates for the AI appeal generator.


## Decision

- Add simple Django admin registration for the Template model only.
  - It fulfills the requirement for an admin.
  - Beginner-friendly and easy to implement.
  - Works with default Django admin; no extra setup required.

## Consequences

- **Positive:**
  - Easy to manage templates.
  - Minimal code and setup.
  - Meets project requirement.
- **Negative/Risks:**
  - Admin interface is very basic, lacks custom styling.
  - No advanced permission controls.

## Validation

- Measure/rollback:
  - Verify that the admin page lists Templates and allows create/edit/delete.
  - Rollback: Remove `admin.site.register(Template)` if needed.
