# Assignment 2 – Assessing Data Management

## What I Know
My coursework has given me a deeper understanding of data management and how it supports the larger use of data within an organization. I understand the data lifecycle including how data is collected, organized, stored, transformed, and prepared for analysis. My strongest understanding is at the big picture level. I understand how databases, ETL, data warehouses, data lakes, data marts, and data pipelines fit together even though I am still developing the technical depth to build complex data environments independently.

My primary data management experience comes from CIDM 6350 - Data and Information Management, and CIDM 6351 - Business Data Extraction, Transformation, and Load. CIDM 6350 introduced me to relational databases, SQL, data modeling, ER diagrams, primary and foreign keys, and normalization. I can create basic database structures, perform basic SQL operations, and represent relationships through ER diagrams. CIDM 6351 expanded my understanding of data warehouses, data lakes, data marts, data pipelines, and ETL. I also gained practical experience using PostgreSQL through pgAdmin and studied Snowflake concepts.

One of my strongest competencies is understanding the relationship between data management and data analytics. My analytics coursework has reinforced that useful analysis depends on data being organized, accessible, accurate, and properly prepared. I understand how data moves from source systems through storage and transformation before becoming available for analytics.

I also have a broad understanding of how data management fits within an organization's larger technology environment. I may not yet be able to independently engineer every component of a complex data architecture, but I can understand the purpose of those components and how they support analytics and other systems.

## Where I Am Weak
My primary weakness is technical depth. I understand the concepts behind data management, but I am less confident with advanced utilization. Advanced SQL and database design are areas for development. I can perform basic SQL operations and create basic database structures, but I need more experience with complex queries, joins, subqueries, advanced aggregations, database optimization, and larger relational structures. I also want more experience designing databases for complex real world requirements.

My knowledge of Snowflake concepts and data engineering is foundational while my hands on database experience with CIDM 6351 involved PostgreSQL through pgAdmin. I understand the purpose of data warehouses, schemas, ETL processes, and pipelines, but I have limited experience independently building sophisticated data workflows. I want to become more comfortable developing pipelines that handle larger, more complex, and changing datasets. Python is another area for improvement. I have used Python and Jupyter Notebook for basic data preparation, but I need greater proficiency with programming, automation, data processing, and integrating Python into larger data workflows. Overall, I understand the architecture and purpose of data management better than I understand the technical aspects.

## What I Wish I Knew and What I May Be Missing
The primary area I want to develop is the ability to move from understanding a data environment to independently building and maintaining one. I understand what databases, ETL processes, and data pipelines accomplish, but I need more hands on experience designing and implementing them. I would like to become more proficient in advanced SQL, database design, Python, data engineering, Snowflake, and database performance. I also want experience working with larger and less structured datasets where issues such as data quality, scalability, automation, reliability, and changing requirements become more important. Ultimately, I want to move beyond understanding the big picture and become more capable of implementing the technical processes that make a well managed data environment possible.

## Supporting Evidence
The following coursework artifacts provide evidence of selected data management skills:

CIDM 6350 – Data and Information Management: The [database schema diagram](artifacts/CIDM-6350/Schema.drawio.pdf) provides evidence of database modeling and schema design.

CIDM 6351 – Business Data Extraction, Transformation, and Load: The pgAdmin screenshot provides evidence of my work with PostgreSQL. My coursework also included SQL queries using a LEFT JOIN with GROUPING SETS, ROLLUP, and CUBE. I completed this query work through a combination of independent effort and guidance, so it demonstrates practical experience while reflecting that I am still developing my ability to write complex queries independently.

CIDM 5310 and CIDM 6308: Coursework in these classes provides additional context for how data preparation and transformation support data analytics.

Jupyter Notebook and JSON: I have used these technologies in my coursework, but I do not currently cite specific artifacts that demonstrate that work.

These artifacts demonstrate selected parts of my coursework, rather than complete proficiency in every aspect of data management. My experience and independence vary by tool and task.

Sources and Resources: My work drew on course materials, my professor's instructions and feedback, database assignments and artifacts from CIDM 6350 and CIDM 6351, and online tutorials and technical documentation. My CIDM 6350 schema diagram and CIDM 6351 PostgreSQL query screenshot provide evidence of my database design and SQL work. These resources supported my understanding of database structure, SQL queries, data organization, and data management practices.

## Contribution Toward the Capstone

## Why Data Management Is Integratable
Data management is integratable with the other curricular areas as it provides the foundation for collecting, organizing, storing, transforming, and preparing information for use. Data analytics uses that information to generate insights and support decisions. Software systems provide applications through which users interact with the information while networking and cybersecurity support connectivity, access, privacy, and protection. Data management therefore provides the structure and reliable information needed for the other areas to function effectively.

## How It Could Be Integrated
For my capstone, Data Management supports the use of real, publicly available California Department of Managed Health Care (DMHC) Independent Medical Review decisions. I use Python to import selected fields into SQLite including reference ID, report year, treatment category, review type, and determination. The application queries these records to calculate historical counts of health plan decisions that were upheld or overturned. Fictional case details are used only to demonstrate the appeal letter workflow.

This approach keeps the prototype manageable while applying concepts from my database and ETL coursework. The historical analysis uses real public DMHC decisions and not synthetic records. Only the example case details entered into the letter form are fictional. The prototype does not use real patient information. A future version using organizational healthcare data would require authorization, appropriate privacy protections, and clear data governance.

## How Data Management Connects to My Prior Work
This concept connects directly to my coursework and existing experience. My healthcare background provides the domain context for understanding healthcare and insurance information. My Data analytics coursework provides experience preparing, analyzing, and interpreting data while my Data management coursework provides a foundation for structuring and storing the information behind an application.

My experience with SQL, PostgreSQL through pgAdmin, ETL concepts, Python, and data preparation could contribute to the project. I have also studied Snowflake concepts although my hands on coursework evidence is from PostgreSQL. In particular, my CIDM 6351 coursework with fact and dimension tables provides a foundation for thinking about how denied claims and related insurance information could be organized. This capstone allows me to strengthen my practical skills in Python, SQL, data quality checks, and database management. Advanced data engineering and additional hands on experience with Snowflake remain future learning goals.

## New Integration Statement
My data management coursework has shown me how structured data supports applications and analysis. In my capstone prototype, I use SQLite to store real, publicly available California DMHC Independent Medical Review decision records rather than synthetic insurance denial records. Python calculates historical counts of upheld and overturned decisions by treatment category, and Django includes these findings in an editable appeal letter draft using fictional case details. The letter is created using a Python template and not a live AI service. Cybersecurity principles guide basic input validation and responsible data handling. This manageable design connects database management, analytics, software development, and privacy without requiring a complex data warehouse or real patient records.

## AI Use
I used AI to help identify gaps in the evidence and capstone integration, and revise the wording of this appraisal with spelling and grammar checks. I used AI to ensure consistent formatting. I reviewed the suggestions and made the final editing decisions.