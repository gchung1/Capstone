# Feedback on Evolution 2: Data Mining and Management

File read: `Capstone/DM/evolution.md`, as committed on 2026-09-18.

## Rubric outcome

| Dimension | Level | Reason |
|---|---|---|
| Completeness and quality | Developing | Sources appear only as categories ("SQL references, database documentation"). The third tier mostly repeats your weaknesses, and the section "How It Could Be Integrated" opens with three sentences from Evolution 1. |
| Evidence and artifacts | Proficient | The diagram and the warehouse project in `Capstone/DM/artifacts/` show data modeling, fact and dimension tables, and SQL. The Snowflake, Jupyter, and JSON claims have no sample, and the appraisal cites no file. |
| Self-assessment accuracy | Proficient | Your weaknesses are specific to the area, and you keep understanding apart from building. |
| Integration thinking | Developing | The new statement opens with your Evolution 1 sentence, "data analytics" changed to "data management", and repeats its chain. |
| Professional presentation | Proficient | Four subsection headings (lines 17, 36, 41, 46) are level-one headings, the same size as the title. |

## What is working

You separate understanding from building. You write that you understand "the architecture and purpose of data management better than" its technical side, and you break "Advanced SQL" down into joins, subqueries, aggregations, and optimization.

Your third tier adds a point that your weaknesses section does not make: less structured data, and the data quality and scalability problems that come with it.

## What needs attention

Add an AI-use line so that a reader knows what help you had. In one sentence, say which tool, if any, helped and with what. At the final commit, this appraisal moves to `portfolio/DM/README.md`.

Say how you wrote the queries in your CIDM 6351 sample. The appraisal lists joins and advanced aggregations as weaknesses. The sample shows a LEFT JOIN with GROUPING SETS, a ROLLUP query, and a CUBE query. If you wrote them in a guided lab or with help, say so. A reader can then judge whether the weakness and the sample agree.

Check the Snowflake claim against your sample. The appraisal assigns Snowflake to CIDM 6351, and the CIDM 6351 file shows PostgreSQL tables in pgAdmin. Cite a sample that shows Snowflake work, or describe the claim as one you cannot yet show.

## Integration readiness

Not yet ready. Your section "How It Could Be Integrated" takes its first three sentences from Evolution 1. Your CIDM 6351 project already holds a data management mechanism: a fact table of trips joined to dimension tables for date, zone, and waste type. The appraisal does not use that design to say how you would organize appeal records.

## Question to carry forward

If you modeled appeals the way you modeled waste collection trips, what would one row of the fact table record, and what would the dimensions be?
