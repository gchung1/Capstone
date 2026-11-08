# ADR-008: Add Class-Based Views for Home and Template Preview

**Date:** 2025-11-18  
**Status:** Accepted

## Context

- Problem/forces:
  - Current project uses function-based views (FBVs) only.
  - We want to introduce **class-based views (CBVs)** as a beginner-friendly alternative for simple pages.
  - Adding CBVs helps standardize view patterns, making future maintenance and extensions easier.
 

## Decision

- Implement `HomeView` and `TemplatePreviewView` as CBVs using Django’s `TemplateView`.  
  - `HomeView` will serve a simple landing page.
  - `TemplatePreviewView` will display the appeal letter template.
  - Use `TemplateView` to minimize code and provide clear examples for beginners.
  - Keep existing FBVs for the main letter generator and PDF download to avoid unnecessary complexity.

## Consequences

- **Positive:**
  - Demonstrates CBV usage for beginners.
  - Cleaner and more consistent view structure for static pages.
  - Easily extendable for future CBVs like FAQ or Privacy pages.
  - Works seamlessly with existing URL namespacing and template links (`{% url 'appeals:home' %}` and `{% url 'appeals:template_preview' %}`).

- **Negative/Risks:**
  - Slight learning curve for developers unfamiliar with CBVs.
  - Minimal extra code for very simple pages (could be seen as over-engineering).

## Validation

- **Measure:**
  - Visit `/home/` and `/template-preview/` successfully renders pages without errors.
  - Navbar links correctly route to the new CBVs using `{% url %}` template tags.

- **Rollback:**
  - Can revert these two pages back to FBVs if CBV pattern causes confusion or issues.
