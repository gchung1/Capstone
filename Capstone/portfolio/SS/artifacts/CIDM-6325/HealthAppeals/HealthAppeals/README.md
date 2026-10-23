## Health Appeal Letter Generator

A Django based, privacy conscious web application that generates AI assisted appeal letters for first-level health insurance denials. The tool allows patients and caregivers to quickly produce draft appeal letters which can then be downloaded or copied.


## Project Overview

Reduce barriers for patients and caregivers in submitting appeals for denied health insurance claims by providing AI powered and or editable letters quickly. PRD is located within the "docs" folder. 


## Key Points:
- Privacy-oriented: no login or persistent data storage
- AI or offline template fallback for letter generation
- Mobile-friendly interface
- Admin interface for managing letter templates

# In Scope Features:
- Web based form for first time appeals
- Dual mode letter generation and save capabilities
- AI letter generation (via OpenAI API)
- Downloadable PDFs or copy/paste letters
- Admin management for templates

# Out of Scope Features:
- Legal or medical advice
- Multi level appeals
- User accounts or tracking beyond anonymous analytics


## Features

# User Facing:
- Form to input treatment, denial reason, doctor recommendation, and additional context
- AI powered letter generation with optional OpenAI API key
- Editable letter output
- Downloadable PDF or copy/paste functionality
- Offline template fallback (dual mode capability)

# Admin Interface:
- Template CRUD (Create, Read, Update, Delete) via ModelForms
- Admin fieldsets for organized template editing
- List, search, and filter templates
- Pagination for template lists

# Technical:
- Class Based Views (CBVs) for homepage and template preview
- QuerySets for filtering, ordering, and limiting templates
- Customizable template previews
- HTTPS ready with Django security middleware


## Rubric Features Implemented

# Good Features (5/4)
1. **(Chapter 2)** include() and namespacing — `urls.py` uses `app_name = 'appeals'` and `include()` for modular routing 
2. **(Chapter 2)** Named URLs and reversing — All templates use `{% url %}` for dynamic linking  
3. **(Chapter 3)** Class Based Views (CBVs) — `HomeView` and `TemplatePreviewView` 
4. **(Chapter 6)** QuerySets - filter/order/limit — `recent_templates()` demonstrates ordering and limiting
5. **(Chapter 7)** ModelAdmin: list/search/filter — `TemplateAdmin` implements `list_display` and `search_fields`

# Better Features (3/2)
1. **(Chapter 4)** Custom template filter — implemented in `apps/appeals/templatetags/letter_filters.py` 
2. **(Chapter 7)** Admin inlines and fieldsets — `TemplateAdmin` uses `fieldsets` to organize template editing
3. **(Chapter 5)** ModelForms for CRUD — admin template views (`admin_template_create/update/delete`) use `TemplateForm`

# Best Features (2/1)
1. **(Chapter 7)** Template overrides and theming — all templates extend `appeals/base.html`, demonstrating inheritance 
2. **(Chapter 8)** Packaging as modular Django app — the project is structured as a reusable Django app (`apps.appeals`)


## Folder Structure

HealthAppeals/
├── apps/
│ └── appeals/
│ ├── init.py
│ ├── admin.py
│ ├── apps.py
│ ├── forms.py
│ ├── models.py
│ ├── tests.py
│ ├── urls.py
│ ├── views.py
│ ├── templatetags/
│ │ ├── init.py
│ │ └── letter_filters.py
│ ├── migrations/
│ │ ├── init.py
│ │ ├── 0001_initial.py
│ │ └── 0002_template_name.py
│ └── templates/
│ ├── appeals/
│ │ ├── base.html
│ │ ├── form.html
│ │ ├── home.html
│ │ └── template_preview.html
│ └── appeals_admin/
│ ├── template_confirm_delete.html
│ ├── template_form.html
│ └── template_list.html
├── health_appeals/
│ ├── init.py
│ ├── asgi.py
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
├── docs/
│ ├── adrs/
│ └── briefs/
├── db.sqlite3
└── manage.py
-README.md


## Quickstart

# Create and Activate Virtual Environment
python -m venv .venv
source .venv/bin/activate 

# Install Dependencies
pip install -r requirements.txt

# Run Migrations
python manage.py makemigrations
python manage.py migrate

# Run Development Server
python manage.py runserver


## Usage
- Access the site at http://127.0.0.1:8000/
- Fill in the appeal form and optionally provide OpenAI API key
- Preview or download the generated letter as PDF
- Admin can add/update/delete templates via /appeals/admin/templates/


## Technical Architecture
Backend: Django 5.2.6, SQLite database

# Models:
Template — stores reusable letter templates

# Forms:
- AppealForm — user-facing input
- TemplateForm — admin CRUD operations

# Views:
- CBVs: HomeView, TemplatePreviewView
- Function-based views: generate_letter, download_pdf, admin CRUD

# Templates:
- appeals/base.html — base layout, navigation, Bootstrap 5
- Inheritance for all user/admin templates

# AI Integration/Dual Mode:
- Optional OpenAI API key for dynamic letter generation
- Offline template  for privacy or offline use

# PDF Generation:
Uses reportlab to render downloadable PDF letters


## Testing
- Basic test ensures the generate_letter page loads (status code 200):
python manage.py test appeals


## References:
- Kaiser Family Foundation (2021). Claims denials and appeals
- Korba, C., Hoadley, J., & Lucia, K. W. (2020). Understanding consumer experiences with insurance appeals. Journal of Health Politics, Policy and Law, 45(6), 967–989
- U.S. Department of Labor. Your rights after a denial of a health claim: How to appeal
- CMS. How to appeal a health insurance company decision