from django import forms
from django.core.validators import FileExtensionValidator
from django.http import QueryDict
from Class_Types import *
from Class_Types.Embeded_Documents import *
import datetime


class BaseForm(forms.Form):

    def __init__(self, data, request=None, *args, **kwargs):
        if isinstance(data, QueryDict):
            updated_data = data.dict()
        else:
            updated_data = data

        if 'id' in updated_data.keys() and updated_data.get('id') != '' and request:
            updated_data.update({'lastModifiedUser': request.user.username})
            updated_data.update({'lastModifiedTimestamp': datetime.datetime.now()})
            super(BaseForm, self).__init__(data=updated_data)
            self.fields['id'] = forms.CharField(max_length=50, required=False)
            self.fields['lastModifiedUser'] = forms.CharField(max_length=50, required=False)
            self.fields['lastModifiedTimestamp'] = forms.DateTimeField(required=False)
            self.fields['createdUser'] = forms.CharField(max_length=50, required=False)
            self.fields['createdTimestamp'] = forms.DateTimeField(required=False)
        elif request:
            updated_data.update({'createdUser': request.user.username})
            updated_data.update({'createdTimestamp': datetime.datetime.now()})
            super(BaseForm, self).__init__(data=updated_data)
            self.fields['createdUser'] = forms.CharField(max_length=50, required=False)
            self.fields['createdTimestamp'] = forms.DateTimeField(required=False)
        else:
            super(BaseForm, self).__init__(data=updated_data)

    def to_model(self):
        assert hasattr(self, 'cleaned_data') and self.cleaned_data
        return self.Meta.model(**self.cleaned_data)


"""SUB FORMS"""


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
        fields = ('addressLineOne', 'addressLineTwo', 'city', 'state', 'zip', 'country')


class NameForm(forms.Form):
    firstName = forms.CharField(max_length=150, required=True)
    lastName = forms.CharField(max_length=150)

    class Meta:
        model = Employee
        fields = ('firstName', 'lastName')


class MultiCharField(forms.MultiValueField):
    def __init__(self, count, *args, **kwargs):
        # Or define a different message for each field.
        field_list = []
        for i in range(count):
            field_list.append(forms.CharField())

        super(MultiCharField, self).__init__(
            fields=tuple(field_list),
            require_all_fields=False, *args, **kwargs
        )

    def compress(self, data_list):
        return '|'.join(map(str, data_list))


class DescriptionForm(forms.Form):
    def __init__(self, count=0, *args, **kwargs):
        super(DescriptionForm, self).__init__(*args, **kwargs)
        self.fields['description'] = MultiCharField(count=count)


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

    class Meta:
        model = Customer


class EmployeeForm(BaseForm):
    userName = forms.CharField(max_length=50, required=True)  # Should be unique
    birthDate = forms.DateField(required=True)
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=20, required=True)
    pin = forms.CharField(max_length=4, required=True)
    rateOfPay = forms.DecimalField()
    active = forms.BooleanField(required=False)
    type = forms.CharField(max_length=10, required=True)
    name = NameForm()
    address = AddressForm()

    class Meta:
        model = Employee
        fields = (
            'userName', 'birthDate', 'email', 'phone', 'pin', 'rateOfPay', 'active', 'type', 'address')

    def __init__(self, data, request):
        super().__init__(data, request)
        self.name = NameForm(data={'firstName': data.get('name.firstName'), 'lastName': data.get('name.lastName')})
        self.address = AddressForm(data={'addressLineOne': data.get('address.addressLineOne'),
                                         'addressLineTwo': data.get('address.addressLineTwo'),
                                         'city': data.get('address.city'), 'state': data.get('address.state'),
                                         'zip': data.get('address.zip'), 'country': data.get('address.country')})

    def is_valid(self):
        return self.name.is_valid() and self.address.is_valid() and forms.BaseForm.is_valid(self=self)

    def to_model(self):
        assert self.cleaned_data
        name = Name(**self.name.cleaned_data)
        address = Address(**self.address.cleaned_data)
        return self.Meta.model(**self.cleaned_data, name=name, address=address)


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
    noiseOrdinance = forms.BooleanField(required=False)
    timeCutOff = forms.CharField()

    fkRegionCode = forms.CharField(required=True)
    fkMicroRegionCode = forms.CharField(required=True)
    coordinates = CoordinateField()
    active = forms.BooleanField(required=False)
    installationDueDates = InstallDateForm()
    inspectionDueDates = InspectDateForm()
    fiscalWeek = forms.IntegerField(min_value=1, max_value=53)

    class Meta:
        model = Store
        fields = ('storeNumber', 'fkCustomer', 'address', 'phoneNumber', 'region', 'division', 'awardedVendor',
                  'storeManagerName', 'storeManagerEmail', 'opsManagerName', 'opsManagerEmail', 'managerName',
                  'managerEmail', 'overnightManagerName', 'overnightManagerEmail', 'overnightCrew', 'overnightAccess',
                  'noiseOrdinance', 'timeCutOff', 'fkRegionCode', 'fkMicroRegionCode', 'coordinates', 'active',
                  'installationDueDates', 'inspectionDueDates', 'fiscalWeek')

    def __init__(self, data, request):
        super().__init__(data, request)
        self.storeManagerName = NameForm(data={'firstName': data.get('storeManagerName.firstName'),
                                               'lastName': data.get('storeManagerName.lastName')})
        self.opsManagerName = NameForm(
            data={'firstName': data.get('opsManagerName.firstName'), 'lastName': data.get('opsManagerName.lastName')})
        self.managerName = NameForm(
            data={'firstName': data.get('managerName.firstName'), 'lastName': data.get('managerName.lastName')})
        self.overnightManagerName = NameForm(data={'firstName': data.get('overnightManagerName.firstName'),
                                                   'lastName': data.get('overnightManagerName.lastName')})
        self.address = AddressForm(data={'addressLineOne': data.get('address.addressLineOne'),
                                         'addressLineTwo': data.get('address.addressLineTwo'),
                                         'city': data.get('address.city'), 'state': data.get('address.state'),
                                         'zip': data.get('address.zip'), 'country': data.get('address.country')})

        self.overnightAccess = DaysOfWeekForm(data={'overnightAccess': data.getlist('overnightAccess')})
        self.inspectionDueDates = InspectDateForm(count=len(data.getlist('inspectionDueDates')),
                                                  data={'inspectionDueDates': data.getlist('inspectionDueDates')})
        self.installationDueDates = InstallDateForm(count=len(data.getlist('installationDueDates')),
                                                    data={'installationDueDates': data.getlist('installationDueDates')})

        self.coordinates = CoordinateField(
            data={'latitude': data.get('coordinates.latitude'), 'longitude': data.get('coordinates.longitude')})

    def is_valid(self):
        return self.storeManagerName.is_valid() and self.opsManagerName.is_valid() and self.managerName.is_valid() and \
               self.overnightManagerName.is_valid() and self.installationDueDates.is_valid() and \
               self.inspectionDueDates.is_valid() and self.address.is_valid() and self.overnightAccess.is_valid() \
               and forms.BaseForm.is_valid(self=self) and self.coordinates.is_valid()

    def to_model(self):
        assert self.cleaned_data
        store_manager_name = Name(**self.storeManagerName.cleaned_data)
        ops_manager_name = Name(**self.opsManagerName.cleaned_data)
        manager_name = Name(**self.managerName.cleaned_data)
        overnight_manager_name = Name(**self.overnightManagerName.cleaned_data)
        address = Address(**self.address.cleaned_data)
        inspection_due_dates = self.inspectionDueDates.cleaned_data['inspectionDueDates'].split('|')
        installation_due_dates = self.installationDueDates.cleaned_data['installationDueDates'].split('|')
        overnight_access = self.overnightAccess.cleaned_data['overnightAccess']
        coordinates = Coordinates(**self.coordinates.cleaned_data)
        return self.Meta.model(**self.cleaned_data, storeManagerName=store_manager_name,
                               opsManagerName=ops_manager_name,
                               managerName=manager_name, overnightManagerName=overnight_manager_name, address=address,
                               inspectionDueDates=inspection_due_dates, installationDueDates=installation_due_dates,
                               overnightAccess=overnight_access,
                               coordinates=coordinates)


class RegionForm(BaseForm):
    regionCode = forms.CharField(max_length=12, required=True)

    class Meta:
        model = RegionCode


class MicroRegionForm(BaseForm):
    microRegionCode = forms.CharField(max_length=12, required=True)

    class Meta:
        model = MicroRegionCode


class WorkOrderForm(BaseForm):
    workOrderName = forms.CharField(required=True, max_length=15)
    dateReceived = forms.DateField(required=True)
    detail = forms.CharField()
    requestingContact = forms.CharField(required=True)
    priority = forms.CharField(required=True)
    statusCode = forms.CharField(required=True, max_length=30)

    dateCompleted = forms.DateField(required=True)
    inspectForStoreFile = forms.FileField(required=False, allow_empty_file=True,
                                          validators=[FileExtensionValidator(['pdf', 'txt'])])
    detailedReceiptFile = forms.FileField(required=False, allow_empty_file=True,
                                          validators=[FileExtensionValidator(['pdf', 'txt'])])
    signageMapFile = forms.FileField(required=False, allow_empty_file=True,
                                     validators=[FileExtensionValidator(['pdf', 'txt'])])
    partsArrivalDate = forms.DateField()

    targetStartDate = forms.DateField(required=True)
    fkWorkOrderStatus = forms.CharField(required=True)
    fkStoreNumber = forms.CharField(required=True)

    class Meta:
        model = WorkOrder
        fields = (
            'workOrderName', 'dateReceived', 'detail', 'requestingContact', 'priority', 'statusCode', 'dateCompleted',
            'inspectForStorePath', 'detailedReceiptPath', 'signageMapPath', 'partsArrivalDate', 'targetStartDate',
            'fkWorkOrderStatus', 'fkStoreNumber')

    def __init__(self, data, request, files):
        super().__init__(data, request)
        self.files = files

    def is_valid(self):
        return BaseForm.is_valid(self)


class WorkOrderStatusForm(BaseForm):
    status = forms.CharField(required=True, max_length=50)

    class Meta:
        model = WorkOrderStatus
        fields = 'status'


class ScopeOfWorkForm(BaseForm):
    GB_Counter = forms.IntegerField(min_value=0)
    GB_CounterBillable = forms.IntegerField(min_value=0)
    SOWPicturePath = forms.ImageField(required=True)
    WrongLocation = forms.BooleanField(required=False)
    ConcretePatchNeeded = forms.BooleanField(required=False)
    fkRightSOWID = forms.CharField(required=True)
    fkStatusID = forms.CharField(required=True)
    completedPicturePath = forms.ImageField(required=False)
    dateFieldEditedStatus = forms.DateField()
    timeFieldEditedStatus = forms.DateTimeField()
    approvedBilling = forms.BooleanField(required=False)
    fkInstallerID = forms.CharField(required=True)
    fkRequireMaterials = forms.CharField(required=True)
    fkLocationInStoreID = forms.CharField(required=True)
    fkWorkOrderID = forms.CharField(required=True)
    fkInitialLaborID = forms.CharField(required=True)
    fkExtraLaborID = forms.CharField(required=True)
    fkCorrectLaborID = forms.CharField(required=True)

    class Meta:
        model = ScopeOfWork
        fields = (
            'GB_Counter', 'GB_CounterBillable', 'SOWPicturePath', 'WrongLocation', 'ConcretePatchNeeded',
            'fkRightSOWID',
            'fkStatusID', 'completedPicturePath', 'dateFieldEditedStatus', 'timeFieldEditedStatus', 'approvedBilling',
            'fkInstallerID', 'fkRequireMaterials', 'fkLocationInStoreID', 'fkWorkOrderID', 'fkInitialLaborID',
            'fkExtraLaborID',
            'fkCorrectLaborID')


class ScopeOfWorkStatusForm(BaseForm):
    status = forms.CharField(required=True, max_length=50)

    class Meta:
        model = ScopeOfWorkStatus
        fields = 'status'


class LaborItemForm(BaseForm):
    quantity = forms.IntegerField(min_value=1)
    fkArticleNumberState = forms.CharField(required=True)

    class Meta:
        model = LaborItem
        fields = ('quantity', 'fkArticleNumberState')


class ArticleNumberStateForm(BaseForm):
    state = forms.CharField(max_length=2, min_length=2, required=True)
    price = forms.DecimalField(required=True, decimal_places=2)
    fkArticleNumber = forms.CharField(required=True)

    class Meta:
        model = ArticleNumberState
        fields = ('state', 'price', 'fkArticleNumber',)


class ArticleNumberForm(BaseForm):
    articleNumber = forms.CharField()
    description = DescriptionForm()  # Make this a list of Strings
    usedByInspectionCompanyButNotPrSkate = forms.BooleanField(required=False)
    capital = forms.BooleanField(required=False)

    class Meta:
        model = ArticleNumber
        fields = ('articleNumber', 'description', 'usedByInspectionCompanyButNotPrSkate', 'capital')

    def __init__(self, data, request):
        super().__init__(data, request)
        self.description = DescriptionForm(count=len(data.getlist('description')),
                                           data={'description': data.getlist('description')})

    def is_valid(self):
        return forms.BaseForm.is_valid(self) and self.description.is_valid()


class MaterialItemForm(BaseForm):
    materialArticleNumber = forms.CharField(required=True)
    description = DescriptionForm()  # Make this a list of Strings

    class Meta:
        model = MaterialItem
        fields = ('materialArticleNumber', 'description')

    def __init__(self, data, request):
        super().__init__(data, request)
        self.description = DescriptionForm(count=len(data.getlist('description')),
                                           data={'description': data.getlist('description')})

    def is_valid(self):
        return forms.BaseForm.is_valid(self) and self.description.is_valid()


class MaterialListForm(BaseForm):
    fkMaterialItem = forms.CharField()  # Make a list of references (forms should be a list of Char fields)

    class Meta:
        model = MaterialList
        fields = 'fkMaterialItem'


class LocationInStoreForm(BaseForm):
    department = forms.CharField(required=True)  # Should be unique with aisle, bay, tower, fkStoreNumber
    aisle = forms.CharField(required=True)
    bay = forms.CharField(required=True)
    tower = forms.CharField(required=True)
    level = forms.CharField(required=True)
    plumbingInLocation = forms.BooleanField(required=False)
    plumbingPicturePath = forms.ImageField()
    plumbingPicturePath2 = forms.ImageField()
    electricalInLocation = forms.BooleanField(required=False)
    electricalPicturePath = forms.ImageField()
    electricalPicturePath2 = forms.ImageField()
    fkMaterialList = forms.CharField(required=True)
    fkStoreNumber = forms.CharField(required=True)

    class Meta:
        model = LocationInStore
        fields = (
            'department', 'aisle', 'bay', 'tower', 'level', 'plumbingInLocation', 'plumbingPicturePath',
            'plumbingPicturePath2',
            'electricalInLocation', 'electricalPicturePath', 'electricalPicturePath2', 'fkMaterialList',
            'fkStoreNumber')

    def __init__(self, data, request, files):
        super().__init__(data, request)
        self.files = files

    def is_valid(self):
        return BaseForm.is_valid(self)


class PrepWorkForm(BaseForm):
    downloadMLX = forms.BooleanField(required=False)
    excelInspectUploaded = forms.BooleanField(required=False)
    inspectionPictures = forms.BooleanField(required=False)
    postedSync = forms.BooleanField(required=False)
    formComplete = forms.BooleanField(required=False)
    concretePatchNeeded = forms.BooleanField(required=False)
    materialOrderNumberHD = forms.CharField()
    cpn_eta = forms.DateTimeField()
    inspectionDueDates = forms.DateTimeField()
    lastDateChecked = forms.DateTimeField()
    fkWorkOrderName = forms.CharField(required=True)

    class Meta:
        model = PrepWork
        fields = (
            'downloadMLX', 'excelInspectUploaded', 'inspectionPictures', 'postedSync', 'formComplete',
            'concretePatchNeeded',
            'materialOrderNumberHD', 'cpn_eta', 'inspectionDueDates', 'lastDateChecked', 'fkWorkOrderName')


class OrderMaterialForm(BaseForm):
    quantity = forms.IntegerField(min_value=1, required=True)
    fkMaterialItem = forms.CharField(required=True)

    class Meta:
        model = OrderMaterial
        fields = ('quantity', 'fkMaterialItem')
