from django import forms
from datetime import datetime as dt
from Class_Types import *
from Class_Types.Embeded_Documents import *


class BaseForm(forms.Form):
    createdUser = forms.CharField(max_length=50, required=False)
    lastModifiedUser = forms.CharField(max_length=50, required=False)
    lastModifiedTimestamp = forms.DateTimeField(required=False)
    createdTimestamp = forms.DateTimeField(required=False)

    def __init__(self, data, request):
        updated_data = data.dict()
        updated_data.update({'createdUser': request.user.username})
        super().__init__(data=updated_data)


"""SUBFORMS"""


class CoordinateField(forms.Form):
    latitude = forms.DecimalField()
    longitude = forms.DecimalField()

    class Meta:
        model = Coordinates
        fields = ('latitude', 'longitude')


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


# noinspection PyArgumentList

class MultiDateField(forms.MultiValueField):
    def __init__(self, count, *args, **kwargs):
        # Or define a different message for each field.
        field_list = []
        for i in range(count):
            field_list.append(forms.DateField())

        super(MultiDateField, self).__init__(
            fields=tuple(field_list),
            require_all_fields=False, *args, **kwargs
        )

    def compress(self, data_list):
        return '|'.join(map(str, data_list))


class InspectDateForm(forms.Form):
    def __init__(self, count=0, *args, **kwargs):
        super(InspectDateForm, self).__init__(*args, **kwargs)
        self.fields['inspectionDueDates'] = MultiDateField(count=count)


class InstallDateForm(forms.Form):
    def __init__(self, count=0, *args, **kwargs):
        super(InstallDateForm, self).__init__(*args, **kwargs)
        self.fields['installationDueDates'] = MultiDateField(count=count)


class DaysOfWeekForm(forms.Form):
    OPTIONS = (
        ('SUN', 'Sunday'),
        ('MON', 'Monday'),
        ('TUES', 'Tuesday'),
        ('WED', 'Wednesday'),
        ('THURS', 'Thursday'),
        ('FRI', 'Friday'),
        ('SAT', 'Saturday')
    )
    overnightAccess = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=OPTIONS)


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

    def __init__(self, data, request):
        super().__init__(data, request)
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
    overnightAccess = DaysOfWeekForm()
    noiseOrdinance = forms.BooleanField()
    timeCutOff = forms.CharField()

    fkRegionCode = forms.CharField(required=True)
    fkMicroRegionCode = forms.CharField(required=True)
    coordinates = CoordinateField()
    active = forms.BooleanField()
    installationDueDates = InstallDateForm()
    inspectionDueDates = InspectDateForm()
    fiscalWeek = forms.IntegerField(min_value=1, max_value=53)

    def __init__(self, data, request):
        super().__init__(data, request)
        self.storeManagerName = NameForm(data={'firstName': data.get('storeManagerNameFirst'),
                                               'lastName': data.get('storeManagerNameLast')})
        self.opsManagerName = NameForm(
            data={'firstName': data.get('opsManagerNameFirst'), 'lastName': data.get('opsManagerNameLast')})
        self.managerName = NameForm(
            data={'firstName': data.get('managerNameFirst'), 'lastName': data.get('managerNameLast')})
        self.overnightManagerName = NameForm(data={'firstName': data.get('overnightNameFirst'),
                                                   'lastName': data.get('overnightNameLast')})
        self.address = AddressForm(data=data)

        self.overnightAccess = DaysOfWeekForm(data={'overnightAccess': data.getlist('overnightAccess')})
        self.inspectionDueDates = InspectDateForm(count=len(data.getlist('inspectionDueDates')),
                                                  data={'inspectionDueDates': data.getlist('inspectionDueDates')})
        self.installationDueDates = InstallDateForm(count=len(data.getlist('installationDueDates')),
                                                    data={'installationDueDates': data.getlist('installationDueDates')})

        self.coordinates = CoordinateField(data={'latitude': data.get('latitude'), 'longitude': data.get('longitude')})

    def is_valid(self):
        test = self.storeManagerName.is_valid()
        test1 = self.opsManagerName.is_valid()
        test2 = self.managerName.is_valid()
        test3 = self.overnightManagerName.is_valid()
        test4 = self.installationDueDates.is_valid()
        test5 = self.inspectionDueDates.is_valid()
        test6 = self.address.is_valid()
        test7 = self.overnightAccess.is_valid()
        test8 = forms.BaseForm.is_valid(self=self)
        test9 = self.coordinates.is_valid()
        return True

    class Meta:
        model = Store
        fields = ('storeNumber', 'fkCustomer', 'address', 'phoneNumber', 'region', 'division', 'awardedVendor',
                  'storeManagerName', 'storeManagerEmail', 'opsManagerName', 'opsManagerEmail', 'managerName',
                  'managerEmail', 'overnightManagerName', 'overnightManagerEmail', 'overnightCrew', 'overnightAccess',
                  'noiseOrdinance', 'timeCutOff', 'fkRegionCode', 'fkMicroRegionCode', 'active',
                  'installationDueDates', 'inspectionDueDates', 'fiscalWeek')


class RegionForm(BaseForm):
    regionCode = forms.CharField(max_length=12, required=True)

    model = RegionCode


class MicroRegionForm(BaseForm):
    regionCode = forms.CharField(max_length=12, required=True)

    model = MicroRegionCode


class WorkOrderForm(BaseForm):
    workOrderName = forms.CharField(required=True, max_length=15)
    dateReceived = forms.DateField(required=True)
    detail = forms.CharField(required=True)
    requestingContact = forms.CharField(required=True)
    statusCode = forms.CharField(required=True, max_length=30)

    dateCompleted = forms.DateField(required=True)
    inspectForStorePath = forms.FileField(allow_empty_file=True)
    detailedReceiptPath = forms.FileField(allow_empty_file=True)
    signageMapPath = forms.FileField(allow_empty_file=True)
    partsArrivalDate = forms.DateField()

    targetStartDate = forms.DateField(required=True)
    fkWorkOrderStatus = forms.CharField(required=True)
    fkStoreNumber = forms.CharField(required=True)

    model = WorkOrder

class WorkOrderStatusForm(BaseForm):
    status = forms.CharField(required=True, max_length=50)

    model= WorkOrderStatus
    fields = 'status'
