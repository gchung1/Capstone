# BRIEF: Build Blog Post CRUD slice

Goal

- Implement blog post CRUD (Create, Read, Update, Delete) and model in the myblog app addressing PRD §blog-mvp-0-1.

Scope (single PR)

- Files to touch:
  - myblog/models.py (Post model: title, slug, body, published_at, is_published, created_at, updated_at)
  - myblog/forms.py (PostForm for admin/user input)
  - myblog/views.py (CRUD views: list, detail, create, update, delete)
  - myblog/urls.py (URL patterns for CRUD)
  - myblog/templates/myblog/post_list.html
  - myblog/templates/myblog/post_detail.html
  - myblog/templates/myblog/post_form.html
  - myblog/templates/myblog/post_confirm_delete.html
  - myblog/tests/test_models.py
  - myblog/tests/test_views.py
  - migrations/ (generated)
- Non-goals:
  - Comments, tags, rich-text editor, RSS/feeds, or external blogging packages.

Standards

- Commits: conventional style (feat/fix/docs/refactor/chore).
- No secrets; env via settings.
- Django tests: use unittest/Django TestCase (no pytest).
- Use Django generic CBVs for CRUD where possible.
- Templates extend base.html and use Django form helpers.

Acceptance

- User flow:
  - User/admin can create, view, edit, and delete blog posts.
  - /blog/ shows paginated list of published posts.
  - /blog/<slug>/ shows post detail.
  - /blog/new/, /blog/<slug>/edit/, /blog/<slug>/delete/ for CRUD actions.
- Include migration? yes
- Update docs & PR checklist.

Prompts for Copilot

- "Generate a Django Post model (fields: title, slug, body, published_at, is_published, created_at, updated_at) with get_absolute_url."
- "Create a ModelForm for Post."
- "Implement CBV-based CRUD views for Post (ListView, DetailView, CreateView, UpdateView, DeleteView)."
- "Add URL patterns for CRUD views."
- "Generate templates for list, detail, form, and confirm delete."
- "Write Django TestCase tests for model and CRUD views."
- "Explain changes and propose commit messages."