from tkinter import Widget
from .models import Entries
from django import forms

class Entries_form(forms.ModelForm):
    class Meta:
        model=Entries
        fields=['name','email','city']
        widgets={
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'city': forms.TextInput(attrs={'class':'form-control'}),
        }