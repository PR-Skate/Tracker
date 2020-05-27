import re

from django import forms
from django.forms import ModelForm, inlineformset_factory, BaseInlineFormSet
from django.forms.utils import ErrorList

from Class_Types import *
from django.forms import widgets


class BaseForm(forms.Form):
    id = forms.CharField(max_length=50)
    createdUser = forms.CharField(max_length=50)
    lastModifiedUser = forms.CharField(max_length=50)
    lastModifiedTimeStamp = forms.DateTimeField()
    createdTimeStamp = forms.DateTimeField()


"""SUBFORMS"""


class CoordinateField(forms.Form):
    latitude = forms.DecimalField()
    longitude = forms.DecimalField()


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
        fields = ('firstName', 'lastName')


class MultiDateField(forms.MultiValueField):
    def __init__(self, **kwargs):
        # Or define a different message for each field.
        fields = (
            forms.DateField(
            ),
        )
        super().__init__(
            fields=fields,
            require_all_fields=False, **kwargs
        )


class MyDateForm(forms.Form):
    inspectDates = MultiDateField()
    model = Store
    fields = ('inspectDates')


class DaysOfWeekField(forms.Form):
    OPTIONS = (
        ('SUN', 'Sunday'),
        ('MON', 'Monday'),
        ('TUES', 'Tuesday'),
        ('WED', 'Wednesday'),
        ('THURS', 'Thursday'),
        ('FRI', 'Friday'),
        ('SAT', 'Saturday')
    )
    days = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=OPTIONS)


"""BASE FORMS"""


class CustomerForm(BaseForm):
    customerName = forms.CharField(max_length=50, required=True)


class EmployeeForm(BaseForm):
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
        self.name = NameForm(data={'firstName': data.get('firstName'), 'lastName': data.get('lastName')})
        self.address = AddressForm(data=data)

    def is_valid(self):
        return self.name.is_valid() and self.address.is_valid() and forms.BaseForm.is_valid(self=self)

    class Meta:
        model = Employee
        fields = ('userName', 'birthDate', 'email', 'phone', 'pin', 'rateOfPay', 'active', 'passwordHash', 'type')


class StoreForm(BaseForm):
    storeNumber = forms.CharField(max_length=50, required=True)
    fkCustomer = forms.CharField(max_length=50, required=True)
    address = AddressForm()
    phoneNumber = forms.CharField(max_length=20, required=True)
    region = forms.CharField(max_length=50, required=True)

    division = forms.CharField(max_length=50, required=True)
    awardedVendor = forms.CharField(max_length=50, required=True)
    storeManagerName = NameForm()
    storeManagerEmail = forms.EmailField()

    opsManagerName = NameForm()
    opsManagerEmail = forms.EmailField()
    managerName = NameForm()
    managerEmail = forms.EmailField()
    overnightManagerName = NameForm()

    overnightManagerEmail = forms.EmailField()
    overnightCrew = forms.CharField(max_length=25)
    overnightAccess = DaysOfWeekField()
    noiseOrdinance = forms.BooleanField()
    timeCutOff = forms.CharField()

    fkRegionCode = forms.CharField(max_length=12, required=True)
    fkMicroRegionCode = forms.CharField(max_length=12, required=True)
    coordinates = CoordinateField()
    active = forms.BooleanField()
    installationDueDates = MultiDateField()
    inspectionDueDates = MultiDateField()
    fiscalWeek = forms.IntegerField(min_value=1, max_value=53)

    def __init__(self, request, data):
        super().__init__(request)
        self.storeManagerName = NameForm(data={'firstName': data.get('storeManagerNameFirst'), 'lastName': data.get('storeManagerNameLast')})
        self.opsManagerName = NameForm(data={'firstName': data.get('opsManagerNameFirst'), 'lastName': data.get('opsManagerNameLast')})
        self.managerName = NameForm(data={'firstName': data.get('managerFirstName'), 'lastName': data.get('managerLastName')})
        self.overnightManagerName = NameForm(data={'firstName': data.get('overnightNameFirst'), 'lastName': data.get('overnightNameFirst')})

        self.address = AddressForm(data={'firstName': data.get('firstName'), 'lastName': data.get('lastName')})


