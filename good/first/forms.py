from django.forms import ModelForm
from first.models import First


class FirstForm(ModelForm):
    class Meta:
        model = First
        # fields = ['name', 'age', 'image']
        fields = '__all__'
