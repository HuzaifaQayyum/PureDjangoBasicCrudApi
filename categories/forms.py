from django import forms

class CategoryForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, min_length=3)