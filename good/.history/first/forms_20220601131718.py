from attr import field, fields
from django.forms import forms

class FirstForm(forms.Form):
    fields = '__all__'