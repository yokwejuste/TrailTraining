from xml.parsers.expat import model
from django.forms import forms
from first.models import First


class FirstForm(forms.Form):
    
    class meta:
        models = First
        fields = '__all__'
        exclude = ['id']
