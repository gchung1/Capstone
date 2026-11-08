# ADR-006: Bootstrap Styling for Health Appeal Generator

Date: 2025-11-14
Status: Accepted

## Context

- Problem/forces:
  - Current website design is very basic and unappealing.
  - Need a responsive, clean layout for better user experience.
  - Must maintain current disclaimers, buttons, forms, and PDF download functionality.


## Decision

- B) Integrate **Bootstrap 5** framework to enhance design:
    - Navbar
    - Buttons
    - Alerts
    - Responsive layout
    -  Provides a simple, beginner-friendly way to improve the visual design while maintaining functionality

## Consequences

- Positive:
  - Professional, clean look with minimal CSS effort.
  - Responsive design on mobile and desktop.
  - Easy to maintain and expand in the future.
- Negative/Risks:
  - Slight increase in page load due to Bootstrap CDN.
  - Developers must be familiar with Bootstrap classes for future changes.

## Validation

- Measure/rollback:
  - Verify all pages render correctly on desktop and mobile.
  - Ensure form submission, PDF download, and disclaimers work as expected.
  - Rollback by removing Bootstrap links and restoring old CSS if needed.
