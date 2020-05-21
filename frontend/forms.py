

from django import forms

class CustomerForm(forms.Form):
    createdUser = forms.CharField(max_length=50, required=True)
    customerName = forms.CharField(max_length=50, required=True)

