from django import forms
from . import models


class PrepositionModelForm(forms.ModelForm):
    class Meta:
        model = models.PrepositionModel
        fields = ['category', 'text', 'file']
        widgets = {
            'category': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'text': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'type': 'text'
                }
            ),
            'file': forms.MultipleHiddenInput(
                attrs={
                    'multiple': True,
                    'class': 'form-control',
                    'name': 'file',
                    'type': 'file'
                }
            ),
        }
