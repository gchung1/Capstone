# ADR-0001: Django Personal Blog Example

Date: 2025-10-10  
Status: Proposed

Context

- PRD link: <#blog-mvp-0-1>
- Problem/forces:
  - The project needs a simple, maintainable blog feature for publishing and viewing posts.
  - Requirements: minimal dependencies, admin-editable posts, paginated list and detail views, basic templates, and test coverage.
  - Constraints: avoid full CMS complexity, keep codebase small, and ensure easy future extensibility.

Options

- A) Build a custom Django app ("myblog") with a minimal Post model, admin registration, list/detail views, and simple templates.
- B) Integrate a third-party Django blog package (e.g., django-blog-zinnia) for more features but with added dependency and integration overhead.

Decision

- We choose A) Build a custom Django app because it:
  - Minimizes dependencies and security surface area.
  - Keeps the codebase simple and maintainable.
  - Satisfies MVP requirements and allows incremental feature growth.

Consequences

- Positive:
  - Full control over data model, templates, and URLs.
  - Easier to test, maintain, and extend.
  - Seamless integration with existing project structure.
- Negative/Risks:
  - Initial feature set is limited (no tags, comments, feeds).
  - Future enhancements (e.g., search, tagging) will require custom development.

Validation

- Measure/rollback:
  - Acceptance: /blog/ lists published posts, /blog/<slug>/ shows post detail, admin can manage posts.
  - Automated tests for model, views, and templates.
  - Rollback: Remove myblog app and migrations if requirements change.