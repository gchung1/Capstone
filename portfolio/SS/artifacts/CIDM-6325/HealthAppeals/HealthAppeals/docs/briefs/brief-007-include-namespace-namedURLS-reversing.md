# CPBrief-007: URL Namespacing and Named URL Reversing for Health Appeal Generator

**Summary:**  
Implement URL namespacing using `app_name` and named URLs with `reverse()` and `{% url %}` in the Health Appeal Generator to improve maintainability and reduce hardcoding of links.

**Rationale:**  
- Current URLs are simple but may become hard to maintain as the project grows.  
- Namespacing prevents conflicts between apps and allows clean organization.  
- Named URLs allow templates and views to reference routes dynamically, making refactoring easier.  

**Implementation Notes:**  
- Define `app_name = "appeals"` in `urls.py`.  
- Use `include()` if multiple apps exist to organize routes.  
- Use `path()` with `name` attributes for all routes.  
- Update templates to use `{% url 'appeals:generate_letter' %}` and `{% url 'appeals:download_pdf' %}`.  
- Update views to use `reverse('appeals:download_pdf')` where needed for redirects or links.  
- Ensure all existing functionality (form submission, PDF download, AI letter generation) continues to work.  

**Benefits:**  
- Easier maintenance if URLs change.  
- Reduces risk of broken links in templates or views.  
- Provides a beginner-friendly demonstration of Django best practices.  

**Risks / Considerations:**  
- Slight learning curve for beginners unfamiliar with namespacing.  
- Developers must consistently use named URLs to maintain benefits.  

**Validation:**  
- **Measure:**  
  - All internal links and redirects function correctly without hardcoded paths.  
  - Application runs without 404 errors on any internal route.  
- **Rollback:**  
  - Revert to previous hardcoded URLs in templates and views if issues occur.
