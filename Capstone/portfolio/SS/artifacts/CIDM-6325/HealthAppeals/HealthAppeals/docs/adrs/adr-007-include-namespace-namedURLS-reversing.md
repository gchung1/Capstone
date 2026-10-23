# ADR-007: Implement URL Namespacing and Named URL Reversing

Date: 2025-11-17  
Status: Accepted

## Context

- Problem/forces:
  - We need to organize URLs for multiple views in the health appeal generator project.
  - We want to avoid hardcoding URLs in templates to simplify maintenance.
  - Beginners in Django need a clear example of reusable URL patterns.


## Decision

- Implement (namespace URLs with `include()` and `app_name`) and use **named URLs** because:
  - Namespacing prevents URL conflicts when multiple apps exist.
  - Named URLs (`reverse()` in views, `{% url %}` in templates) allow dynamic linking.
  - Makes templates and views more maintainable and readable.

## Consequences

- Positive:
  - Easier maintenance if URL patterns change.
  - Beginner-friendly demonstration of Django’s routing system.
  - Allows smooth integration with redirecting and linking features (e.g., success messages).  
- Negative/Risks:
  - Slight learning curve for students unfamiliar with `include()` and namespacing.
  - Extra layer of indirection when reading URLs in templates and views.

## Validation

- Measure:
  - All links in the template use `{% url 'appeals:generate_letter' %}` or `reverse('appeals:download_pdf')`.
  - The application runs without 404 errors for any internal link.
- Rollback:
  - Could revert to hardcoded paths if named URL resolution fails.
