from django import forms


class AppealForm(forms.Form):
    treatment_category = forms.CharField(
        label="Treatment Category",
        max_length=100
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