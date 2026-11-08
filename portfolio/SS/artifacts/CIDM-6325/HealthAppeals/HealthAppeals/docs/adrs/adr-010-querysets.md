# ADR-010: Implement Recent Templates Feature Using QuerySets

**Date:** 2025-11-19  
**Status:** Accepted

## Context

- Need to display the most recent templates efficiently in views or dashboards.  
- Fetching all templates and filtering in Python is inefficient.  
- Using Django ORM QuerySets enables cleaner, more performant code.  
- The implementation should remain beginner-friendly while demonstrating filtering, ordering, and limiting.


## Decision

- A simple, reusable function leveraging QuerySets for sorting and limiting results.  
- Keeps the code beginner-friendly and avoids unnecessary complexity.  
- Implement a utility function `recent_templates` returning a limited number of recent templates via a      QuerySet:  
  - Uses `Template.objects.all().order_by('-id')[:limit]`.  
  - Default limit = 5.  
  - Reusable in multiple views or template contexts. 

## Positive / Benefits

- Efficient database query fetching only the needed templates.  
- Demonstrates QuerySet filtering, ordering, and slicing for learning purposes.  
- Reusable in multiple views or templates.  
- Minimal, easy-to-maintain code.  

## Negative / Risks

- Relies on `id` to represent creation order; may not match actual timestamps if IDs are manually set.  
- No input validation for `limit`; extreme values could return unexpected results.  
- Limited to "recent by ID" ordering; advanced filtering (e.g., by date) requires modification.  

## Validation

- Call the `recent_templates()` function in a view or template context.  
- Verify it returns the last `limit` templates in descending ID order.  
- Test with default, custom, and boundary limit values.  
- Confirm results match the database entries.  

## Rollback

- Replace usage of `recent_templates()` with `Template.objects.all()` and perform filtering/sorting in Python if necessary.  
- Remove calls to the function from views and templates until the issue is resolved.
