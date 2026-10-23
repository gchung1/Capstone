from django import forms
from .models import Template

class AppealForm(forms.Form):
    treatment = forms.CharField(label="Treatment Denied", max_length=200)
    denial_reason = forms.CharField(label="Denial Reason", max_length=300)
    doctor_recommendation = forms.CharField(label="Doctor Recommendation", max_length=300)
    additional_info = forms.CharField(
        label="Additional Information", 
        widget=forms.Textarea(attrs={'rows': 2}), 
        required=False
        )
    openai_key = forms.CharField(label="Your OpenAI API Key (optional)", max_length=100, required=False)


class TemplateForm(forms.ModelForm):
    class Meta:
        model = Template
        fields = ['name', 'text']