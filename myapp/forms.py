from django import forms
from .models import myModel

class myModelForm(forms.ModelForm):
    class Meta:
        model = myModel
        fields = ('title', 'description')
