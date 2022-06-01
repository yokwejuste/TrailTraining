from django import forms
from first.models import First


class FirstForm(forms.ModelForm):
    class Meta:
        models = First
        fields = ['name', 'age', 'image']
