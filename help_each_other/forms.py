from . import models
from django import forms


class CreateCharity(forms.ModelForm):
    class Meta:
        model = models.Charity
        fields = ['description', 'image', 'address']

        widgets = {
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Describe your charity'}),
        }