from django import forms
from .models import pre_home

class PreHomeForm(forms.ModelForm):
    class Meta:
        model = pre_home
        fields = ['user', 'club']