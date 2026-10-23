# Project Pitch: AI Powered Appeal Letter Generator for Healthcare Insurance Denials

Problem Statement: Patients in the United States frequently encounter denials of insurance coverage for necessary medical treatments, medications, and procedures. According to a 2021 Kaiser Family Foundation report, 18% of in-network claims in ACA compliant plans are denied. While patients have the legal right to appeal, the process is often confusing and labor-intensive, especially for individuals facing health crises, time constraints, limited health literacy, or language barriers. 
A key barrier is the creation of a compelling, well-structured appeal letter that includes pertinent medical details, references to policy or clinical justification, and correct formatting. Existing templates tend to be generic and do not reflect the nuances of individual situations. The idea is to help people get a strong first draft without needing legal or medical writing skills.

Stakeholders:	
•	Patients/Caregivers – need guidance writing personalized, clear, and effective appeal letters under tight time constraints
•	Patient Advocates – need efficient tools to assist large volumes of clients
•	Clinics/Providers – want to support patients in appealing denials but lack the time to draft letters or knowledge of a reliable resource for assistance
•	Insurers (indirectly) – gain efficiency through more accurate appeals, reducing prolonged follow-up communication and enabling faster care communication

Project Scope: This project will create a simple, web-based tool that helps people write appeal letters when their health insurance denies coverage for a treatment, procedure, or medication. This version of the tool is focused only on basic first-time appeals, which is the first step when an insurance company denies treatment or medication. More advanced or legal steps such as hiring a lawyer or filing formal complaints are not part of this version.
1.	User will answer a few questions
o	What was denied (e.g., "physical therapy for a back injury")
o	Why the insurance said no (e.g., “not medically necessary”)
o	Who the doctor is and what they recommended
o	Any other details the user wants to include to support the appeal
2.	The tool will then use artificial intelligence (AI) such as ChatGPT to automatically create a personalized first draft letter
3.	The user can read, edit, and download based on the information provided to send to their insurance company




What the web-based tool will not do:
•	It will not ask user to create an account or setup login
•	It will not store any personal information
•	It will not provide specific insurance company requirements, guidelines, or information
•	It will not give legal or medical advice
o	Clear transparency message of AI Usage – clear disclaimer to 100% of users that the letter is AI generated, may contain inaccuracies, and is not a substitute for legal or medical advice

Success Metrics:
•	Time to Generate Letter – user to generate and download a draft letter in under 5 minutes
•	Readability – generate letters at middle school to early high school reading level
•	User Satisfaction (simulated survey) – at least 80% of users rate the letters as “ready to use/only minor edits needed”
•	User Retention – at least 30% of users return to use the tool again which is tracked via site traffic tracker


Minimum Viable Artifact (MVA):
•	Simple Django-based web form where users can input necessary information to develop a draft appeal letter
•	Integration with AI (or LLM) for letter generation via a template
•	Editable text area with the generated letter
•	Download/export feature (PDF or copy to clipboard)
•	Admin-only backend to CRUD appeal templates and sample letters
•	AI disclaimer and privacy message informing users the letter was AI generated and might need edits, is not legal and/or medical advice, and no personal information is stored
•	Mobile friendly design (consideration)


Evidence Base:
•	Kaiser Family Foundation. (2021). Claims denials and appeals in ACA marketplace plans. https://www.kff.org/health-reform/issue-brief/claims-denials-and-appeals-in-aca-marketplace-plans/ 
o	Highlights high denial rates and low appeal rates due to process complexity
•	Korba, C., Hoadley, J., & Lucia, K. W. (2020). Understanding consumer experiences with insurance appeals. Journal of Health Politics, Policy and Law, 45(6), 967–989. https://doi.org/10.1215/03616878-8641543
o	Shows lack of support tools results in appeal fatigue
•	U.S. Department of Labor. (n.d.). Your rights after a denial of a health claim: How to appeal. https://www.dol.gov/sites/dolgov/files/EBSA/about-ebsa/our-activities/resource-center/publications/your-rights-after-a-denial-of-a-health-claim.pdf
o	Federal standards that define patient rights and outline the need for clear, timely appeals
•	Centers for Medicare & Medicaid Services. (n.d.). How to appeal a health insurance company decision. U.S. Department of Health & Human Services. Retrieved September 11, 2025, from https://www.cms.gov/CCIIO/Resources/Files/Downloads/appeals-process.pdf
o	How to appeal a health insurance company decision

System Sketch (User Side):
User (stakeholder exception of insurance company)
        ↓
Simple Web Form
(User fills in denial details)
        ↓
Send Information to AI Service
(AI writes the appeal letter draft)
        ↓
Show Letter to User
(User reads and edits the letter)
        ↓
Download or Copy Letter
(User saves or shares the letter)


System Sketch (Admin Side):
Site Admin
        ↓
Manage Templates
(Add or edit letter templates for AI)
        ↓
Update System Settings
(Keep things running smoothly)


Risk Register:
•	AI Error/False Claims
o	Include AI disclaimer on every output
o	Encourage user to check AI generated letter aligns with formatting and individual insurance company guidelines
•	AI Privacy Concerns
o	Do not save input data
o	No login credentials or account required
o	Use https only
