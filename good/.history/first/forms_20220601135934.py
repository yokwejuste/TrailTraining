from django.forms import 
from first.models import First


class FirstForm(forms.ModelForm):
    class Meta:
        model = First
        fields = ['name', 'age', 'image']
