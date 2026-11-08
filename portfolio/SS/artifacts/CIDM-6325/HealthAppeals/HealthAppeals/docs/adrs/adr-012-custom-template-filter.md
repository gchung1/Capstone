# ADR-012: Add Custom Template Filters for Letter Output Cleanup

**Date:** 2025-11-20  
**Status:** Accepted

## Context

- The project renders AI-generated or offline fallback appeal letters in Django templates.  
- Some generated letters may have inconsistent whitespace, lowercase openings, or other formatting irregularities.  
- The course rubric includes “Better” features such as **custom template tags/filters**.  
- The codebase must remain beginner-friendly, and new features should be **additive only**.  
- Custom template filters allow improved letter display formatting **without altering generation logic**.


## Decision

- Implement a custom template filters provide display formatting improvements without changing the underlying generation logic.  
- Add a `templatetags` module with filters that:  
  - Clean extra whitespace.  
  - Capitalize sentences.  
  - Standardize insurer names.  
  - Optional usage in templates; no impact on existing views or models.  

## Positive / Benefits

- Improves readability of AI/offline generated letters.  
- Fully additive — no existing views or models modified.  
- Meets the “Better” rubric requirement.  
- Filters are isolated, maintainable, and beginner-friendly.  

## Negative / Risks

- Filters affect only display, not PDF output unless applied there later.  
- Developers must remember to load filters in templates to apply them.  
- Misuse or overuse of filters could cause inconsistent formatting.  

## Validation

- Submit the appeal form and confirm letters display cleaner when filters are used.  
- Verify application behavior remains unchanged if filters are not applied.  
- Ensure AI and offline templates remain unmodified.  
- Confirm Django successfully loads the `templatetags` module.  
- Test filters individually with simple strings to verify correctness.  

## Rollback

- Delete the `templatetags` module file for letter filters.  
- Remove `{% load letter_filters %}` and any usage like `|clean_whitespace` from templates.  
- No changes to views or models require rollback.
