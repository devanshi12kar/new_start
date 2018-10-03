from django import forms

from home.models import Image

class Image(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['name']
