# ADR-003: Dual-Mode Letter Generation System (OpenAI + Offline Template)

Date: 2025-11-14
Status: Accepted

## Context

- Problem/forces:
  - Some users may have an OpenAI API key, while others may not.
  - The system needs to provide AI-generated letters for users with a key.
  - Users without a key should still be able to generate letters via an offline template.
  - Must maintain disclaimers about AI-generated content.


## Decision

- Dual-mode because it maximizes usability for all users and ensures the project works without forcing OpenAI account creation.

## Consequences

- Positive:
  - Users without OpenAI accounts can still use the system.
  - Flexible for both AI and offline templates.
  - Keeps disclaimers clear.
- Negative/Risks:
  - Slightly more complex implementation logic in the backend.
  - Need to maintain offline templates for accuracy.

## Validation

- Measure/rollback:
  - Test both modes:
    - With OpenAI API key: ensure AI-generated letter is produced.
    - Without API key: ensure offline template letter is produced.
  - Rollback by removing offline template logic if it causes errors (temporary solution).
