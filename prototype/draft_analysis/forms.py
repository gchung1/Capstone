
from django import forms
from .models import DMHCDecision


class AppealForm(forms.Form):
    treatment_category = forms.ChoiceField(
        label="Treatment Category"
    )

    denial_reason = forms.CharField(
        label="Denial Reason",
        max_length=100
    )

    justification = forms.CharField(
        label="Fictional Medical Necessity Explanation",
        widget=forms.Textarea,
        max_length=1000
    )

    supporting_documents = forms.CharField(
        label="Available Supporting Documents",
        widget=forms.Textarea,
        required=False,
        max_length=500
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        categories = (
            DMHCDecision.objects
            .order_by("treatment_category")
            .values_list("treatment_category", flat=True)
            .distinct()
        )

        self.fields["treatment_category"].choices = [
            ("", "Select a treatment category")
        ] + [(category, category) for category in categories]
