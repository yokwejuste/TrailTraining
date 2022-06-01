from xml.parsers.expat import model
from django import forms
from first.models import First


class FirstForm(forms.Mode:
    class meta:
        models = First
        fields = '__all__'
