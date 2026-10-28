# Feedback on Evolution 3: Systems Development

File read: `Capstone/SS/evolution.md`, as committed on 2026-10-08.

## Rubric outcome

| Dimension | Level | Reason |
|---|---|---|
| Completeness and quality | Developing | The appraisal lists no sources you consulted. The third tier, on AI-assisted development, is new and your own. |
| Evidence and artifacts | Developing | The appraisal cites no file. `Capstone/SS/artifacts/` holds a link to a personal repository and the CIDM 6375 ransomware answers, which do not show software work. |
| Self-assessment accuracy | Developing | Your weaknesses stay general ("integrating multiple technologies"), and you describe CIDM 6325 as HTML and basic web development, although its repository holds a Django application. |
| Integration thinking | Developing | The new statement repeats your earlier four-part chain and uses no mechanism from your own software work. |
| Professional presentation | Strong | The appraisal renders cleanly, follows the prompt's parts, and runs about 1,160 words. |

## What is working

Your third tier makes an argument of your own. You treat AI tools as "an accelerator for my software skills rather than a replacement for them", and you give the reason: your knowledge of the business problem, the data, and the security concerns lets you judge whether a generated solution addresses the problem.

You rank Software and Systems as your weakest area in the first paragraph, and your new statement returns to that ranking.

## What needs attention

Copy the HealthAppeals files that show your CIDM 6325 work into `Capstone/SS/artifacts/CIDM-6325/`. The file there holds only an address, and a personal repository can change after I read it. Add an AI-use line so that a reader knows what help you had. In one sentence, say which tool, if any, helped and with what. At the final commit, this appraisal moves to `portfolio/SS/README.md`.

Describe your CIDM 6325 work as the repository shows it. The appraisal lists "HTML, Git/GitHub, VS Code, project organization, and basic web development". The linked repository holds a Django application with models, views, forms, an admin interface for templates, and 14 architecture decision records. Its requirements document describes an "AI Powered Appeal Letter Generator for Health Insurance Denials", the concept you propose for the capstone. Say which parts you built without help and which with help, so that your weaknesses rest on that work.

## Integration readiness

Not yet ready. Your new statement repeats the chain in your Evolution 1 and 2 statements (manage, analyze, present, protect). HealthAppeals already contains a software mechanism. Its form collects the denied treatment, the denial reason, and the doctor's recommendation. Its view sends these to a language model when the user supplies an OpenAI key, and fills a fixed letter template when the user does not. The integration section does not use it.

## Question to carry forward

Which of your 14 HealthAppeals decision records would you keep for the prototype, and which would you change?
