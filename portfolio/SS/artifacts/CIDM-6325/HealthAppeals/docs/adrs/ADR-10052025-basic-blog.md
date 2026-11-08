# ADR-0001: Create a simple blog page in the myblog Django app

Date: 2025-10-05  
Status: Accepted

Context

- PRD link: <#section-or-issue> (add link to product requirements)
- We need a simple, maintainable blog page for the site to publish posts and allow readers to view a post list and post detail. The site currently uses Django and has an app area for features; a small dedicated app ("myblog") is appropriate.
- Goals: minimal dependencies, easy to maintain, test coverage, support for title, body, publish date, optional slug, and admin editing.
- Constraints: keep implementation lightweight (no full CMS), support migrations and Django admin, integrate with existing site styling and templates.

Options

- A) Implement a simple blog inside the "myblog" app:
  - Create Post model (title, slug, body, published_at, is_published).
  - Register model in admin with basic list/display fields.
  - Add list view (paginated) and detail view (by slug or pk).
  - Create two templates (myblog/post_list.html, myblog/post_detail.html).
  - Add URLs (e.g., /blog/ and /blog/<slug>/) and include in project urls.py.
  - Add simple unit tests (model, views, templates).
  - Keep styling minimal and reuse site base template.

- B) Use a third-party blogging package (e.g., django-blog-zinnia, django-blog-it):
  - Faster feature set (comments, tags, feeds) but adds external dependency, upgrades to manage, and potential integration overhead.

- C) Use Django flatpages or a CMS:
  - Could be overkill for simple blog needs; requires learning/config and more surface area to secure.

Decision

- We choose A) Implement a simple blog inside the "myblog" app because it:
  - Minimizes external dependencies and security surface area.
  - Keeps codebase small and easy to understand for the team.
  - Satisfies immediate product requirements and is extensible later (tags, comments, RSS) if needed.

Consequences

- Positive:
  - Full control over data model, templates, and URLs.
  - Easier to test and reason about; fewer surprises from external packages.
  - Works well with existing project structure and deployment process.
- Negative / Risks:
  - Will require developer time to implement standard blog features (tagging, feeds, comments) if requested later.
  - Less feature-rich initially compared to mature blogging packages.
  - Must maintain migrations and model changes over time.

Validation

- Measure:
  - Acceptance criteria: blog index page at /blog/ lists published posts (paginated) and each post is viewable at its detail URL; posts manageable in Django admin.
  - Automated tests: unit tests for the Post model, URL routing, list view returns 200 and shows expected posts, detail view resolves and renders post content.
  - Manual verification: create posts in admin, confirm listing and detail pages render correctly and match site layout.
- Rollback:
  - Revert the commit(s) that add the myblog app and associated migrations, remove myblog from INSTALLED_APPS, and run migrate to roll back DB schema changes if needed.