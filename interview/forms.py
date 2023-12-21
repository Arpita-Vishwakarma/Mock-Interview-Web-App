from django import forms
from .models import InterviewInformation

class InterviewForm(forms.ModelForm):
    class Meta:
        model = InterviewInformation
        fields = '__all__'