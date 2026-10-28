# Feedback on the capstone proposal

Files read: `Capstone/proposal/proposal.md` and `Capstone/proposal/diagram.png`, as committed on 2026-10-23 (03ed749).

## Decision: revise before greenlight

An appeal letter helper builds on your HealthAppeals work, and the Django interface is a sound choice. Three requirements are not met, and the revision must correct all three. First, the proposal does not identify one user and the action that user takes. Second, the data are 30 to 50 synthetic records with no real reference. Third, the letter workflow and the analytics are two separate outputs rather than one path through the areas. Revise the proposal no later than November 2, 2026.

## What I checked

| Check | Level | Reason |
|---|---|---|
| Problem and purpose | Partly met | The pretext lists "patients and health insurance organizations". Choose one user and state the action. |
| Working prototype | Partly met | The interface is clear. The inputs are too few, and the path splits into two outputs. |
| Prototype synthesis | Partly met | BA summarizes records that the letter user never touches. CN "guides" but nothing breaks without it. |
| Synthesis paper | Partly met | The full project lists additions but not how each area needs the others. |
| Portfolio traceability | Partly met | Section 8 cites `Capstone/BA/evolution.md` and similar paths. The files are `Capstone/portfolio/BA/README.md` and so on. |
| Architecture and feasibility | Not met | The synthetic data have no generator and no real reference. The language model API is not identified. The milestone has no evidence file. |
| Presentation readiness | Partly met | A demonstration of a letter is possible. The analytics would show only invented patterns. |

Form: commit the proposal as `proposal/proposal.md` and the diagram beside it. The diagram is a hub with two-way arrows. Redraw it as a flow in the order of section 2.

## Tool approvals

SQLite and Django: approved. The language model API: not approved until you name it and give a mode that a reviewer can run without your key.

## Numbered questions

Revise the proposal, and answer each question by number in `proposal/consultation-response.md`, no later than November 2, 2026. You may add a recording of up to five minutes and link it from that file.

1. Who uses the prototype, and what decision or action do they take with its output?
2. Which real, public appeal records will you use? Some states publish one record per independent medical review decision. One example, which is my suggestion and not a requirement, is the California Department of Managed Health Care's "Independent Medical Review (IMR) Determinations" dataset, with one record per decision since 2001. Any state's data will do. Whatever you choose, get the data from the agency that publishes it, not from a copy posted on another site (Kaggle and similar sites host copies). Record the agency's URL and your retrieval date in the prototype README, because the agency is the one that answers for the data. Check your choice against the four conditions.
3. Trace one record from the source to the screen. How does the analysis change the letter that the user gets?
4. Which language model API will you call, and what does the prototype do when no key is present?
5. What file will show that your first milestone is done?

Your force-push on 2026-10-23 removed the evolution feedback from `feedback/`. I have added it again. Keep that folder. Line 24 of `Capstone/portfolio/SS/artifacts/CIDM-6325/HealthAppeals/blog_project/settings.py` holds a Django secret key, committed on 2026-10-23. Anyone who can read the repository, now or later, can read a key in a commit. Follow the SECRET_KEY section of Django's deployment checklist (https://docs.djangoproject.com/en/stable/howto/deployment/checklist/#secret-key): generate a new key, load it from an environment variable, and keep it out of the repository. The old key stays in the Git history, so do not use it anywhere.

## What happens next

Revise the proposal and answer the questions no later than November 2, 2026. I review the revision and then give a decision.
