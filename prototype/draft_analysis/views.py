
from django.shortcuts import render
from .forms import AppealForm
from .models import DMHCDecision


def home(request):
    form = AppealForm(request.POST or None)
    submitted = False
    statistics = None
    draft_letter = None

    # Get available years from the DMHC database.
    years = (
        DMHCDecision.objects
        .order_by("-report_year")
        .values_list("report_year", flat=True)
        .distinct()
    )

    selected_year = request.POST.get("report_year", "")

    if request.method == "POST" and form.is_valid():
        submitted = True

        category = form.cleaned_data["treatment_category"].strip()
        review_type = form.cleaned_data["review_type"]
        denial_reason = form.cleaned_data["denial_reason"]
        justification = form.cleaned_data["justification"]
        documents = form.cleaned_data["supporting_documents"] or "Not specified"

        decisions = DMHCDecision.objects.filter(
            treatment_category__iexact=category,
            review_type=review_type
        )

        # Filter historical decisions if a year was selected.
        if selected_year:
            if selected_year.isdigit() and int(selected_year) in years:
                decisions = decisions.filter(report_year=int(selected_year))
            else:
                selected_year = ""

        year_description = selected_year if selected_year else "All Years"

        statistics = {
            "category": category,
            "review_type": review_type,
            "year": year_description,
            "total": decisions.count(),
            "source_ids": list(
                decisions.order_by("reference_id")
                .values_list("reference_id", flat=True)[:3]
            ),
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
                f"for {year_description} include {statistics['total']} decisions "
                f"matching the {category} treatment category and "
                f"{review_type} review type. Of those, "
                f"{statistics['upheld']} upheld the health plan's decision "
                f"and {statistics['overturned']} overturned it. "
                f"These historical figures do not predict the outcome "
                f"of an individual appeal."
            )
        else:
            data_context = (
                f"No matching historical California DMHC decisions "
                f"were found for {year_description}, the {category} treatment "
                f"category, and {review_type} review type."
            )

        draft_letter = (
            "To: Health Plan Appeals Department\n"
            "Subject: Request for Reconsideration of Denied Healthcare Service\n\n"
            "Dear Appeals Reviewer,\n\n"
            "I am requesting reconsideration of a denied healthcare service "
            "based on the following fictional case information.\n\n"
            f"Treatment Category: {category}\n"
            f"Review Type: {review_type}\n"
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
        "years": years,
        "selected_year": selected_year,
    })
