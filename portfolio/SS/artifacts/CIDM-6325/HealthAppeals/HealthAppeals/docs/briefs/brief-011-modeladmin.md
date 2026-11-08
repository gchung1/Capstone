# CPBrief-011: Simplify Django Admin for Template Model

**Summary:**  
Implemented a simplified Django admin interface for the `Template` model, registering a custom `TemplateAdmin` class that only displays existing fields (`id` and `name`) and enables search by `name`, avoiding errors caused by referencing non-existent fields like `created_at`.

**Rationale:**  
- Previous admin configurations caused errors due to non-existent fields in `list_display` and `list_filter`.  
- Admin users need basic functionality to view and search templates without errors.  
- Keeping the admin interface simple maintains beginner-friendly and stable code.

**Implementation Notes:**  
- Registered `TemplateAdmin` with:
  ```python
  @admin.register(Template)
  class TemplateAdmin(admin.ModelAdmin):
      list_display = ('id', 'name')
      search_fields = ('name',)
      list_filter = ()
