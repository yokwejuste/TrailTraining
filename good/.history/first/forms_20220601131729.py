from attr import field, fields
from django.forms import forms

class FirstForm(forms.Form):
    mode
    fields = '__all__'