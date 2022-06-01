from attr import field, fields
from django.forms import forms

class FirstForm(forms.Model):
    fields = '__all__'