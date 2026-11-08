# CPBrief-003: Dual-Mode Letter Generation System (OpenAI + Offline Template)

**Summary:**  
Implement a dual-mode letter generation system that supports both AI-generated letters for users with an OpenAI API key and offline template letters for users without a key. Disclaimers about AI-generated content are maintained in both cases.

**Rationale:**  
- Some users may not have an OpenAI account.  
- Offering both modes ensures accessibility, usability, and inclusivity.  
- Users with API keys can access AI-generated letters, while others can rely on a built-in template.  
- Keeps AI disclaimers visible and consistent.

**Implementation Notes:**  
- Backend checks if the user provides an OpenAI API key.  
- If a key is provided, generate the letter via the OpenAI API.  
- If no key is provided, use a built-in offline template with placeholder content.  
- Maintain current form and PDF download functionality.  
- Include AI disclaimer in both AI-generated and offline template letters.  

**Benefits:**  
- Inclusive for all users, regardless of OpenAI access.  
- Maintains AI disclaimer compliance.  
- Flexible system, easy to extend or update offline templates if needed.  

**Risks / Considerations:**  
- Slightly increased backend complexity.  
- Offline templates need maintenance if legal, insurance, or formatting requirements change.  

**Validation:**  
- **Measure:** Test both modes:  
  - With OpenAI API key → ensure AI-generated letter is produced.  
  - Without API key → ensure offline template letter is produced.  
- **Rollback:** Remove offline template logic temporarily if it causes errors.
