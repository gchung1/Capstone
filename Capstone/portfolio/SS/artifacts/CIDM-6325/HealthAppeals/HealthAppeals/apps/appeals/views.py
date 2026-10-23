from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from io import BytesIO
from .forms import AppealForm
from django.views import View
from django.core.paginator import Paginator
from .models import Template
from .forms import TemplateForm


# Offline template fallback
OFFLINE_TEMPLATE = """
[Your Name]
[Your Address]
[City, State ZIP Code]
[Email Address]
[Phone Number]
[Date]

[Insurance Company Name]
[Claims Department Address]
[City, State ZIP Code]

Subject: Appeal for Denied Treatment

Dear [Insurance Company Name] Claims Review Team,

I am writing to formally appeal the denial of coverage for the following treatment:

Treatment: {treatment}
Reason for Denial: {denial_reason}
Doctor's Recommendation: {doctor_recommendation}
Additional Information: {additional_info}

Based on my doctor's professional recommendation and the medical necessity of this treatment, I respectfully request that you reconsider the decision and approve coverage.

Thank you for your time and attention to this matter. Please let me know if any additional information or documentation is required.

Sincerely,
[Your Name]
"""

def generate_letter(request):
    letter_text = None

    if request.method == "POST":
        form = AppealForm(request.POST)
        if form.is_valid():
            treatment = form.cleaned_data["treatment"]
            denial_reason = form.cleaned_data["denial_reason"]
            doctor_recommendation = form.cleaned_data["doctor_recommendation"]
            additional_info = form.cleaned_data["additional_info"]
            openai_key = form.cleaned_data.get("openai_key")
            request.session["last_treatment"] = form.cleaned_data["treatment"]

            if openai_key:
                # Set API key dynamically
                openai.api_key = openai_key
                prompt = f"""
                Write a first-level insurance appeal letter at grade 7 reading level.
                Include AI disclaimer at the end.

                Treatment denied: {treatment}
                Denial reason: {denial_reason}
                Doctor recommendation: {doctor_recommendation}
                Additional information: {additional_info}
                """
                try:
                    response = openai.chat.completions.create(
                        model="gpt-4o-mini",
                        messages=[{"role": "user", "content": prompt}]
                    )
                    letter_text = response.choices[0].message.content
                except Exception as e:
                    letter_text = f"Error generating AI letter: {str(e)}\n\nUsing offline template instead.\n"
                    letter_text += OFFLINE_TEMPLATE.format(
                        treatment=treatment,
                        denial_reason=denial_reason,
                        doctor_recommendation=doctor_recommendation,
                        additional_info=additional_info
                    )
            else:
                # Use offline template if no API key
                letter_text = OFFLINE_TEMPLATE.format(
                    treatment=treatment,
                    denial_reason=denial_reason,
                    doctor_recommendation=doctor_recommendation,
                    additional_info=additional_info
                )
        # Form invalid POST
        else:
            letter_text = None
    # GET request
    else:
        form = AppealForm()

    # Always render response
    return render(request, "appeals/form.html", {"form": form, "letter": letter_text})


def download_pdf(request):
    text = request.GET.get("text", "")
    buffer = BytesIO()
    p = canvas.Canvas(buffer)

    y = 800
    for line in text.split("\n"):
        p.drawString(50, y, line)
        y -= 15

    p.showPage()
    p.save()
    buffer.seek(0)

    response = HttpResponse(buffer, content_type="application/pdf")
    response["Content-Disposition"] = "attachment; filename=appeal_letter.pdf"
    return response


def home(request):
    return HttpResponse("Welcome to the Health Appeal Generator!")


class HomeView(View):
    """Simple homepage rendered using CBV"""
    template_name = "appeals/home.html"

    def get(self, request):
        return render(request, self.template_name)
    
class TemplatePreviewView(View):
    """Preview the offline fallback letter template with placeholder values."""
    template_name = "appeals/template_preview.html"

    def get(self, request):
        preview_text = OFFLINE_TEMPLATE.format(
            treatment="Example Treatment",
            denial_reason="Example Denial Reason",
            doctor_recommendation="Example doctor recommendation.",
            additional_info="Example supporting details."
        )
        return render(request, self.template_name, {"letter": preview_text})

def template_detail(request, id):
    return HttpResponse(f"Template ID: {id}")


def template_list(request):
    sample_items = list(range(1, 51))  # dummy list
    paginator = Paginator(sample_items, 10)
    page_obj = paginator.get_page(request.GET.get("page"))
    return HttpResponse(f"Page {page_obj.number} items: {page_obj.object_list}")

def recent_templates(limit=5):
    """Return the most recent templates, limited by limit=5."""
    """Demonstrates filter/order/limit QuerySets."""
    
    return Template.objects.all().order_by('-id')[:limit]


# ModelForm for CRUD
# LIST (READ)
def admin_template_list(request):
    templates = Template.objects.all().order_by("-id")
    return render(request, "appeals_admin/template_list.html", {"templates": templates})

# CREATE
def admin_template_create(request):
    form = TemplateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("appeals:admin_template_list")
    return render(request, "appeals_admin/template_form.html", {"form": form, "title": "Add Template"})

# UPDATE
def admin_template_update(request, pk):
    template = Template.objects.get(pk=pk)
    form = TemplateForm(request.POST or None, instance=template)
    if form.is_valid():
        form.save()
        return redirect("appeals:admin_template_list")
    return render(request, "appeals_admin/template_form.html", {"form": form, "title": "Edit Template"})

# DELETE
def admin_template_delete(request, pk):
    template = Template.objects.get(pk=pk)
    if request.method == "POST":
        template.delete()
        return redirect("appeals:admin_template_list")
    return render(request, "appeals_admin/template_confirm_delete.html", {"template": template})