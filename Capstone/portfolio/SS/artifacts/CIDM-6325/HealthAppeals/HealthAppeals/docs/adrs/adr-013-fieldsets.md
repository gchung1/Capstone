# ADR-013: Add Fieldsets to Template Admin

**Date:** 2025-11-21  
**Status:** Accepted

## Context

- The `Template` model in the appeals app currently has a simple Django admin interface.  
- All fields are displayed in a single form, which can become confusing as the project grows.  
- The PRD specifies: *“Admin backend for updating templates”*, but the current admin layout is not beginner-friendly.  
- There are no related models yet, so inlines are not applicable at this stage.  


## Decision

- Implement a grouped fieldsets to improve admin usability without affecting existing models or backend logic.  
- Add `fieldsets` to the `TemplateAdmin` to group fields into logical sections:  
  - `"Template Information"` for the `name` field.  
  - `"Template Content"` for the `text` field with an explanatory description.  
  - Beginner-friendly and fully additive; compatible with existing templates.  

## Positive / Benefits

- Beginner-friendly layout for admins.  
- Fully additive — no existing code or model changes.  
- Improves usability without introducing complexity.  
- Compatible with existing templates and future extensions.  

## Negative / Risks

- No inlines added yet; related models would require separate ADR and updates.  
- Admin users must understand which section contains which fields.  
- Minor risk of admins ignoring the description provided for the `text` field.  

## Validation

- Open Django admin and edit a `Template` instance.  
- Confirm the `name` and `text` fields appear in separate, labeled sections.  
- Confirm the description under the `text` field displays correctly.  
- Verify the list view still shows `id` and `name`.  
- Ensure normal add/update/delete operations behave correctly.  

## Rollback

- Remove the `fieldsets` configuration from `TemplateAdmin`.  
- No changes to models or views require rollback.  
- Admin reverts to the default single-form layout.  
