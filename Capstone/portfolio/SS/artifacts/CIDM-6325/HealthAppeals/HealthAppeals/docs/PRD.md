# Title: AI Powered Appeal Letter Generator for Health Insurance Denials


Overview: A simple, privacy conscious web tool that helps patients generate personalized AI powered appeal letters in response to insurance denials for treatments, procedures, or medications. The goal is to reduce barriers in the appeal process by using a large language model to create a first draft letter in under 5 minutes with minimal user input.


Context: Patients in the United States frequently face insurance denials. 18% of in-network claims are denied, and less than 1% of denied claims are appealed. Despite having the legal right to appeal, only a small percentage of individuals do so, often due to time constraints, health challenges, or confusion about the process. Generating an appeal letter is one of the most difficult yet essential steps in an appeals process. Templates are often too generic, and legal and medical writing can be challenging. Ultimately, lack of consumer friendly tools contribute to overall appeal fatigue. This project aims to close that gap.


In-Scope:
•	Web-based form for first-time health insurance appeals
•	Letter generation via AI (LLM such as ChatGPT)
•	Download or copy functionality
•	Privacy oriented - no login or data storage
•	Admin interface for updating templates


Out-of-Scope:
•	Legal and medical advice
•	Appeals beyond first-level denial
•	Insurance specific appeal instructions
•	Account creation or user data tracking beyond anonymous visit tracking


Use Cases/User Stories:
•	As a patient, I want to generate a personalized appeal letter in under 5 minutes so that I can submit to my insurance company within the tight time and circumstantial constraints.
•	As a caregiver, I want to help someone I support get an appeal letter written quickly and accurately.
•	As a provider/clinic staff/patient advocate, I want to refer patients to a tool that generates draft appeal letters so I can support more patients despite time limitations and various language barriers.
•	As an insurance company, we want to be able to efficiently approve appeals, reduce prolonged communication, and enable faster care.


Functional Requirements:
•	Web form collects key information:
o	Denied treatment or medication
o	Denial reason
o	Doctor’s recommendation
o	Additional user provided context
•	AI integration to generate personalized letter
•	Editable version of generated letter
•	Downloadable PDF feature as or copy/paste functionality
•	Mobile friendly interface
•	Admin backend to:
o	Manage templates (add, update, delete)
o	Test output
•	Display AI disclaimer on every output


Non-Functional Requirements:
•	Letter generation time of under 5 minutes
•	Middle school to early high school reading level
•	Privacy:
o	No account or login creation
o	No data storage
•	HTTPS enforced for security purposes
•	Monthly uptime of 99.5%


Dependencies:
•	LLM service such as ChatGPT
•	Web hosting
•	Django framework
•	PDF generation
•	Analytics tool for anonymous usage tracking


Risks:
•	AI generates misleading or inaccurate content
•	Misuse of the tool for non-healthcare related purposes
•	User(s) assume legal and medical validity of AI output
•	Lack of support for insurance specific requirements and guidelines


Assumptions:
•	User(s) will review and edit letters accordingly prior to sending to the insurance company
•	Tool will be used for basic first level denials only
•	AI service will be reliable and cost effective
•	Majority of users will access via mobile or desktop browser


Success Metrics:
•	Time to Generate Letter – 90% of users able to generate and download a draft letter in under 5 minutes
•	Readability – generate letters at grade 6-9 reading level
•	Download Functionality – 100% of users able to download a PDF or copy/paste letter
•	AI Disclaimer – disclaimer visible with every letter output
•	Privacy Disclaimer – disclaimer visible with every user input
•	User Satisfaction Feedback – at least 80% of users rate the letters as “ready to use/only minor edits needed”
•	User Retention – at least 30% of users return to use the tool again which is tracked via anonymous site traffic tracker
•	Crash/Error Rate – less than 1% per 100 sessions


Release Timeline:

Phase	Milestone	Timeline
MVP Dev	Build Django-based form + AI integration	Week 1–3
Internal Test	Admin adds templates	Week 4
Pilot Launch	Release to limited audience (patient advocates)	Week 5
Feedback Loop	Collect feedback + adjust templates	Week 6
Public Beta	Broader release + add analytics tracking	Week 7
v1 Launch	Stable release + mobile optimization	Week 8






Open Questions:
•	Would it be valuable and feasible to integrate with provider systems?
•	Could we incorporate multi-language functionality?
o	If so, which languages?
•	Which LLM offers best cost balance, security, and customizability?


References:
Kaiser Family Foundation. (2021, July 14). Claims denials and appeals in ACA marketplace plans. KFF. https://www.kff.org/health-reform/issue-brief/claims-denials-and-appeals-in-aca-marketplace-plans/

Korba, C., Hoadley, J., & Lucia, K. W. (2020). Understanding consumer experiences with insurance appeals. Journal of Health Politics, Policy and Law, 45(6), 967–989. https://doi.org/10.1215/03616878-8641543

U.S. Department of Labor. (n.d.). Your rights after a denial of a health claim: How to appeal. Employee Benefits Security Administration. https://www.dol.gov/sites/dolgov/files/EBSA/about-ebsa/our-activities/resource-center/publications/your-rights-after-a-denial-of-a-health-claim.pdf

Centers for Medicare & Medicaid Services. (n.d.). How to appeal a health insurance company decision. U.S. Department of Health & Human Services. https://www.cms.gov/CCIIO/Resources/Files/Downloads/appeals-process.pdf
