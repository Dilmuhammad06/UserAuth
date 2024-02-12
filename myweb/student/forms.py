from django import forms
from .models import IMages

class ImageForms(forms.ModelForm):
    class Meta:
        model = IMages
        fields = ['name','image']