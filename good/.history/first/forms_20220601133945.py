from xml.parsers.expat import model
from django import forms
from first.models import First


class FirstForm(forms.Form:
    class meta:
        models = First
        fields = '__all__'
