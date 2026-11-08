from django.shortcuts import render
from .forms import AppealForm
from .models import DMHCDecision


def home(request):
    form = AppealForm(request.POST or None)
    submitted = False
    statistics = None
    draft_letter = None

    if request.method == "POST" and form.is_valid():
        submitted = True

        category = form.cleaned_data["treatment_category"].strip()
        denial_reason = form.cleaned_data["denial_reason"]
        justification = form.cleaned_data["justification"]
        documents = form.cleaned_data["supporting_documents"] or "Not specified"

        decisions = DMHCDecision.objects.filter(
            treatment_category__iexact=category
        )

        statistics = {
            "category": category,
            "total": decisions.count(),
            "upheld": decisions.filter(
                determination="Upheld Decision of Health Plan"
            ).count(),
            "overturned": decisions.filter(
                determination="Overturned Decision of Health Plan"
            ).count(),
        }

        if statistics["total"] > 0:
            data_context = (
                f"Historical California DMHC Independent Medical Review data "
                f"include {statistics['total']} decisions in the "
                f"{category} treatment category. Of those, "
                f"{statistics['upheld']} upheld the health plan's decision "
                f"and {statistics['overturned']} overturned it. "
                f"These historical figures do not predict the outcome "
                f"of an individual appeal."
            )
        else:
            data_context = (
                "No matching historical California DMHC decisions "
                "were found for this treatment category."
            )

        draft_letter = (
            "To: Health Plan Appeals Department\n"
            "Subject: Request for Reconsideration of Denied Healthcare Service\n\n"
            "Dear Appeals Reviewer,\n\n"
            "I am requesting reconsideration of a denied healthcare service "
            "based on the following fictional case information.\n\n"
            f"Treatment Category: {category}\n"
            f"Denial Reason: {denial_reason}\n\n"
            f"Medical Necessity Explanation:\n{justification}\n\n"
            f"Available Supporting Documentation:\n{documents}\n\n"
            f"Public Decision Data Context:\n{data_context}\n\n"
            "Please review the medical necessity explanation and available "
            "supporting documentation when reconsidering this decision.\n\n"
            "Sincerely,\n"
            "Appeals Coordinator\n\n"
            "DRAFT — For coordinator review and editing only."
        )

    return render(request, "draft_analysis/home.html", {
        "form": form,
        "submitted": submitted,
        "statistics": statistics,
        "draft_letter": draft_letter,
    })