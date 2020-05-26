import re

from django import forms
from django.forms import ModelForm, inlineformset_factory, BaseInlineFormSet
from Class_Types import *


class AddressForm(forms.Form):
    addressLineOne = forms.CharField(max_length=150, required=True)
    addressLineTwo = forms.CharField(max_length=150, required=False)
    city = forms.CharField(max_length=75, required=True)
    state = forms.CharField(max_length=2, required=True)
    zip = forms.CharField(max_length=5, required=True)
    country = forms.CharField(max_length=75, required=True)

    class Meta:
        model = Address
        fields = ('address.addressLineOne', 'address.addressLineTwo', 'address.city', 'address.state', 'address.zip',
                  'address.country')


class NameForm(forms.Form):
    firstName = forms.CharField(max_length=150, required=True)
    lastName = forms.CharField(max_length=150)

    class Meta:
        model = Employee
        fields = ('name.FirstName', 'name.lastName')


class CustomerForm(forms.Form):
    createdUser = forms.CharField(max_length=50, required=True)
    customerName = forms.CharField(max_length=50, required=True)


class EmployeeForm(forms.Form):
    createdUser = forms.CharField(max_length=50, required=True)
    userName = forms.CharField(max_length=50, required=True)  # Should be unique
    birthDate = forms.DateField(required=True)
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=20, required=True)
    pin = forms.CharField(max_length=4, required=True)
    rateOfPay = forms.DecimalField()
    active = forms.BooleanField()
    passwordHash = forms.CharField(widget=forms.PasswordInput)
    type = forms.CharField(max_length=10, required=True)
    name = NameForm()
    address = AddressForm()

    def __init__(self, request, data):
        super().__init__(request)
        self.name = NameForm(data=data)
        self.address = AddressForm(data=data)

    def is_valid(self):
        return self.name.is_valid() and self.address.is_valid() and forms.BaseForm.is_valid(self=self)

    class Meta:
        model = Employee
        fields = ('userName', 'birthDate', 'email', 'phone', 'pin', 'rateOfPay', 'active', 'passwordHash', 'type')
