from django import forms
from .models import Url
from .utils import random_characters


class UrlForm(forms.ModelForm):
    original = forms.URLField(widget=forms.TextInput(
        attrs={'Placeholder': 'example.com/abc/def/ghi'}))
    path = forms.CharField(required=False)

    class Meta:
        model = Url
        fields = ('original', 'path')

    """If the user does not want to enter the path herself, 
    a random 5-letter character will be generated."""

    def clean(self):
        clean_data = super().clean()

        if not clean_data['path']:
            clean_data['path'] = random_characters()

        return clean_data
