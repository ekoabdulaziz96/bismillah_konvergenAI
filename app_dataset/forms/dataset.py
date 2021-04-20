# membuat form
from django import forms

from app_dataset import models


class DatasetForm(forms.ModelForm):
    error_css_class = 'error'

    class Meta:
        model = models.Dataset
        fields = (
            'name',
            'description',
            'fileDataset',
        )

        labels = {
            'name': 'Nama',
            'description': 'Deskripsi',
            'fileDataset': 'File Dataset (*.zip)',
        }

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'nama dataset',
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'deskripsi/informasi dataset',
                }
            ),
            'fileDataset': forms.ClearableFileInput(
                attrs={
                    'class': 'form-control',
                    'required':'required'
                }
            ),
        }
