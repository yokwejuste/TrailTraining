from xml.parsers.expat import model
from attr import field, fields
from django.forms import forms

class FirstForm(forms.Form):
    model = First()
    fields = '__all__'