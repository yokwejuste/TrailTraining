from xml.parsers.expat import model
from django import forms
from first.models import First


class FirstForm(forms.ModelForm):
    class Meta:
        model = First
        fields = ['name', 'age', 'text']
