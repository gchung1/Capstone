# CPBrief-010: Implement Recent Templates Feature Using QuerySets

**Summary:**  
Added a simple, reusable utility function `recent_templates(limit=5)` to return the most recent templates using Django ORM QuerySets. This improves efficiency by limiting database queries and demonstrates beginner-friendly filtering, ordering, and slicing.

**Rationale:**  
- There is a need to display the most recent templates efficiently in views or dashboards.  
- QuerySets provide better performance than fetching all templates and filtering in Python.  
- Keeping the implementation simple and beginner-friendly ensures maintainability and educational value.

**Implementation Notes:**  
- Created a utility function `recent_templates(limit=5)` in `apps.appeals.utils`:

```python
from .models import Template

def recent_templates(limit=5):
    """
    Return the most recent templates, limited by `limit`.
    Demonstrates filter/order/limit QuerySets.
    """
    return Template.objects.all().order_by('-id')[:limit]

- Defaults to returning the last 5 templates ordered by descending ID.  
- Function can be used in any view, dashboard, or template context that requires showing recent templates.  
- Avoids over-engineering; no custom managers or complex queries needed for this simple use case.  

**Consequences:**  
- **Positive:**  
  - Efficient database query fetching only the needed templates.  
  - Demonstrates Django QuerySet filtering, ordering, and slicing for educational purposes.  
  - Reusable in multiple views or templates.  
  - Minimal additional code, keeps implementation beginner-friendly.  
- **Negative/Risks:**  
  - Relies on `id` to represent creation order; may not match actual creation timestamps if IDs are manually set.  
  - No validation for `limit`; extreme values could return unexpected results.  
  - Function is limited to "recent by ID" ordering; advanced filtering (e.g., by creation date) would require modification.  

**Validation:**  
- **Measure:**  
  - Call `recent_templates()` in a view or template context.  
  - Verify it returns the last `limit` templates in descending ID order.  
  - Test with different `limit` values (default, custom, boundary values).  
  - Confirm results match actual database entries.  
- **Rollback:**  
  - Replace with `Template.objects.all()` and perform filtering/sorting in Python if necessary.  
  - Remove calls to `recent_templates()` from views and templates until the issue is resolved.  
