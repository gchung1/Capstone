# ADR-014: Implement ModelForm CRUD with Bootstrap Admin Pages for Templates

**Date:** 2025-11-22  
**Status:** Accepted

## Context

- The `Template` model exists but lacks a user-friendly interface outside Django admin.  
- PRD specifies a beginner-friendly admin interface for managing templates.  
- Goal: Provide full CRUD (Create, Read, Update, Delete) with Bootstrap styling, consistent with the public site.  


## Decision

- Implement Bootstrap-styled ModelForm CRUD pages.  
- Provides full functionality and consistent visual design.  
- Additive — does not modify existing models or letter generation.  
- Separate CRUD pages using ModelForm and Bootstrap: tables, cards, and buttons for Create/Update/Delete.  

## Positive / Benefits

- Beginner-friendly interface for admins.  
- Full CRUD functionality.  
- Bootstrap-styled to match public site.  
- Templates managed separately from public templates.  

## Negative / Risks

- No authentication; URLs are accessible if known.  
- Risk of accidental deletion mitigated by confirmation pages.  
- Future template changes may require updates to forms and views.  

## Validation

- Confirm listing, creating, editing, and deleting templates work as expected.  
- Ensure Bootstrap styling matches the public site.  
- Verify database changes persist correctly.  

## Rollback

- Remove the CRUD views, forms, URLs, and Bootstrap templates folder.  
- No changes to models; public-facing functionality remains intact.  
