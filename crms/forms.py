from django import forms
from django.db.models import fields
from .models import Writer

class WriterForm(forms.ModelForm):
    class Meta:
        model=Writer
        fields='__all__'
