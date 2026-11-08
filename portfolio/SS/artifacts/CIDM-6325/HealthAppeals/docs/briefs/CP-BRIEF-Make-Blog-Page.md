# BRIEF: Build Simple Blog view slice

Goal

- Implement a simple blog listing and detail view in the myblog app addressing PRD §3.
- Provide a minimal Post model so content can be created, migrated, and managed via Django admin.

Scope (single PR)

- Files to touch:
  - myblog/models.py (Post model: title, slug, body, published_at, is_published, created_at, updated_at)
  - myblog/admin.py (register Post with sensible list_display, search, prepopulated_fields)
  - myblog/views.py (list and detail views)
  - myblog/urls.py (app URL patterns)
  - project urls.py (include myblog.urls)
  - myblog/templates/myblog/post_list.html
  - myblog/templates/myblog/post_detail.html
  - myblog/tests/test_models.py (model behavior) and myblog/tests/test_views.py (views)
  - migrations/ (generated)
- Non-goals:
  - Comments, tags, rich-text editor, RSS/feeds, or external blogging packages.

Model specification

- Model name: Post (in myblog.models)
- Fields:
  - title: CharField(max_length=200)
  - slug: SlugField(max_length=200, unique=True, blank=True)
  - body: TextField()
  - published_at: DateTimeField(null=True, blank=True)
  - is_published: BooleanField(default=False)
  - created_at: DateTimeField(auto_now_add=True)
  - updated_at: DateTimeField(auto_now=True)
- Behavior:
  - Auto-generate a unique slug from title if blank (truncate to allow suffixes).
  - When is_published toggled true and published_at empty, set published_at to timezone.now() on save.
  - get_absolute_url returns namespaced detail URL (slug preferred, fallback to pk).
- Meta:
  - ordering = ['-published_at', '-created_at']
  - add indexes on published_at and slug for fast queries.
- Migrations: Include generated migration in PR (run makemigrations before committing).

Standards

- Commits: conventional style (feat/fix/docs/refactor/chore).
- No secrets; config via settings and environment.
- Django tests: use unittest / Django TestCase (no pytest).
- Templates: extend project base.html; keep markup minimal and accessible.
- Views: prefer class-based ListView and DetailView.

Acceptance

- User flow:
  - /blog/ shows paginated list of published posts ordered by published_at desc.
  - /blog/<slug>/ shows post detail (fallback /blog/<pk>/ also supported).
  - Admin can create/edit posts and set is_published/published_at.
- Include migration? yes
- Update docs & PR checklist: yes — include usage notes, example URLs, and test summary.

Tests

- Model tests:
  - slug auto-generation uniqueness.
  - setting is_published updates published_at when appropriate.
  - get_absolute_url returns expected path.
- View tests:
  - list shows only published posts and paginates.
  - detail resolves by slug and pk and returns 200 for published posts.
  - unpublished posts return 404 from public views.
- Template asserts: key content (title, date, body excerpt) rendered.

Prompts for Copilot

- "Generate a Django Post model (fields and behavior described above) including get_absolute_url and save override."
- "Create myblog/admin.py registering Post with list_display, list_filter, search_fields, prepopulated_fields."
- "Create myblog/views.py using ListView and DetailView to show published posts; include simple pagination and slug/PK lookup fallback."
- "Create myblog/urls.py with patterns for /blog/ and /blog/<slug>/ and show how to include them in project urls.py."
- "Generate two templates: myblog/post_list.html and myblog/post_detail.html that extend base.html and render title, date, and body."
- "Write Django TestCase tests for model behaviors (slug uniqueness, publish timestamp) and for list/detail views."
- "Explain changes and propose concise commit messages: (1) feat(myblog): add Post model and admin, (2) feat(myblog): add list/detail views, urls and templates, (3) test(myblog): add model and view tests."

Checklist before merge

- [ ] Add 'myblog' to INSTALLED_APPS and ensure TEMPLATES.APP_DIRS = True.
- [ ] Run python manage.py makemigrations myblog and include migration file.
- [ ] Run python manage.py migrate and django tests locally.
- [ ] Confirm admin can create/edit Post and public URLs render as expected.
- [ ] Update PR description with acceptance steps and test summary.