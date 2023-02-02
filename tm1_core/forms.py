from django import forms

class Form_year(forms.ModelForm):
    nombre = forms.CharField(max_length=100)