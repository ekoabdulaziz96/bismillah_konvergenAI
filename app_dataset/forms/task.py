# membuat form
from django import forms

from app_dataset import models


class TaskForm(forms.ModelForm):
    error_css_class = 'error'

    class Meta:
        model = models.Task
        fields = (
            'user',
            'dataset',
            'name',
            'description',
        )

        labels = {
            'name': 'Nama',
            'description': 'Deskripsi',
            'fileDataset': 'File Dataset (*.zip)',
        }

        widgets = {
            'user': forms.Select(
                attrs={
                    'class': 'form-control',
                    'required': 'required',
                }
            ),
            'dataset': forms.Select(
                attrs={
                    'class': 'form-control',
                    'required': 'required',
                }
            ),
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'nama task',
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'deskripsi/informasi task',
                }
            ),
        }
