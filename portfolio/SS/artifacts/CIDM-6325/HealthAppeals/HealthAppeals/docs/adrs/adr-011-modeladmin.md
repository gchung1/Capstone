# ADR-011: Add ModelAdmin for Template in Django Admin

**Date:** 2025-11-19  
**Status:** Accepted

## Context

- The project requires an admin interface to manage appeal letter templates.  
- The `Template` model currently has `id` and `name` fields but no `created_at` or other metadata fields.  
- Previous attempts to configure admin failed due to referencing non-existent fields.  
- Admin users benefit from a searchable and manageable list of templates.  


## Decision

- Implement a simple `ModelAdmin` registration using only existing fields.  
- Register a simplified `ModelAdmin` for `Template` with only existing fields:  
  - Display `id` and `name` in the list view.  
  - Enable search by `name`.  
  - No list filters since no suitable fields exist.  
- Provides a functional, searchable admin list without errors.  
- Beginner-friendly and stable setup.  

## Positive / Benefits

- Admins can see templates listed by ID and name.  
- Search by template name is available.  
- Avoids errors due to missing fields.  
- Minimal and maintainable admin code.  

## Negative / Risks

- No filtering options are available without additional model fields.  
- Limited functionality compared to more advanced admin setups.  
- Future model updates may require extending the admin configuration.  

## Validation

- Access Django admin and confirm the template list displays `id` and `name`.  
- Verify searching by `name` works correctly.  
- Confirm no filters are displayed (expected).  
- Create, edit, and delete templates via admin UI without errors.  

## Rollback

- Remove or modify the `TemplateAdmin` registration if issues occur.  
- Temporarily register the model without a custom admin class to revert to default admin behavior.  
