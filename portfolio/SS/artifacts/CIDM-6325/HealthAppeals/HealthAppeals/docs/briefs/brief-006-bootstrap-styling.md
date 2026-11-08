# CPBrief-006: Bootstrap Styling for Health Appeal Generator

**Summary:**  
Integrate Bootstrap 5 into the Health Appeal Generator to improve website appearance and responsiveness while keeping existing features intact (forms, buttons, disclaimers, PDF download).

**Rationale:**  
- Current website is basic and unappealing.  
- Bootstrap provides a beginner-friendly, responsive framework.  
- Enhances user experience without complex custom CSS.

**Implementation Notes:**  
- Include Bootstrap 5 CSS/JS via CDN.  
- Update templates to use Bootstrap classes for:  
  - Navbar  
  - Buttons  
  - Alerts  
  - Forms  
  - Footer  
- Ensure existing disclaimers, form submission, and PDF functionality remain unchanged.

**Benefits:**  
- Clean, professional look with minimal CSS effort.  
- Fully responsive layout for desktop and mobile.  
- Easy to maintain and expand in the future.

**Risks / Considerations:**  
- Slightly increases page load due to Bootstrap CDN.  
- Developers must understand Bootstrap classes for future edits.

**Validation:**  
- **Measure:**  
  - Pages render correctly on desktop and mobile.  
  - Forms, PDF download, and disclaimers function as expected.  
- **Rollback:**  
  - Remove Bootstrap CDN links and revert templates to original CSS if necessary.
