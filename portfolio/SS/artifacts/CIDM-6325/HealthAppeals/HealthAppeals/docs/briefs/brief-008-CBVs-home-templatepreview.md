# CPBrief-008: Add Class-Based Views for Home and Template Preview

**Summary:**  
Introduce two beginner-friendly class-based views (`HomeView` and `TemplatePreviewView`) in the Health Appeal Generator to provide a structured and maintainable approach for simple static pages, while keeping existing function-based views for main functionality.

**Rationale:**  
- Current project relies solely on function-based views (FBVs), which can become repetitive for static pages.  
- CBVs provide a clear, reusable structure, demonstrating best practices to beginners.  
- Using `TemplateView` for these pages keeps code minimal and easy to understand.  
- Maintaining FBVs for the main letter generator ensures no disruption to critical functionality.  

**Implementation Notes:**  
- Create `HomeView` and `TemplatePreviewView` in `apps/appeals/views.py` using `TemplateView`.  
- Add URL patterns with namespacing in `apps/appeals/urls.py`:  
  ```python
  from .views import HomeView, TemplatePreviewView

  urlpatterns = [
      path("home/", HomeView.as_view(), name="home"),
      path("template-preview/", TemplatePreviewView.as_view(), name="template_preview"),
  ]

-Update base.html navigation to include:
<li class="nav-item">
    <a class="nav-link" href="{% url 'appeals:home' %}">Home</a>
</li>
<li class="nav-item">
    <a class="nav-link" href="{% url 'appeals:template_preview' %}">Template Preview</a>
</li>

## Benefits

- Beginner-friendly demonstration of CBVs.
- Cleaner, more maintainable code for simple pages.
- Facilitates future expansion (FAQ, Privacy, About pages).
- Seamless integration with URL namespacing and template links.

## Risks / Considerations

- Slight learning curve for developers unfamiliar with CBVs.
- Extra code for very simple pages might appear unnecessary to some.

## Validation

### Measure

- Visiting `/home/` and `/template-preview/` renders the correct pages.
- Navbar links correctly navigate to the new CBVs.
- Existing FBVs for letter generation and PDF download continue to work.

### Rollback

- Revert `HomeView` and `TemplatePreviewView` to FBVs if CBVs introduce confusion or issues.
