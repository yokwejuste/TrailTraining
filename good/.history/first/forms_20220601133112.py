from xml.parsers.expat import model
from attr import field, fields
from django.forms import forms
from first.models import First


class FirstForm(forms.Form):
    
    class Meta:
        models = First
        fields = '__all__'