from django import forms
from django.core.validators import FileExtensionValidator

from Class_Types import *
from Class_Types.Embeded_Documents import *


class BaseForm(forms.Form):
    lastModifiedUser = forms.CharField(max_length=50, required=False)
    lastModifiedTimestamp = forms.DateTimeField(required=False)
    createdUser = forms.CharField(max_length=50, required=False)
    createdTimestamp = forms.DateTimeField(required=False)

    def __init__(self, data, request):
        updated_data = data.dict()
        if 'id' in updated_data.keys() and updated_data.get('id') != '':
            updated_data.update({'lastModifiedUser': request.user.username})
        else:
            updated_data.update({'createdUser': request.user.username})
        super().__init__(data=updated_data)


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
        fields = (
            'userName', 'birthDate', 'email', 'phone', 'pin', 'rateOfPay', 'active', 'type', 'address')


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
        return self.storeManagerName.is_valid() and self.opsManagerName.is_valid() and self.managerName.is_valid() and \
               self.overnightManagerName.is_valid() and self.installationDueDates.is_valid() and \
               self.inspectionDueDates.is_valid() and self.address.is_valid() and self.overnightAccess.is_valid() \
               and forms.BaseForm.is_valid(self=self)

    class Meta:
        model = Store
        fields = ('storeNumber', 'fkCustomer', 'address', 'phoneNumber', 'region', 'division', 'awardedVendor',
                  'storeManagerName', 'storeManagerEmail', 'opsManagerName', 'opsManagerEmail', 'managerName',
                  'managerEmail', 'overnightManagerName', 'overnightManagerEmail', 'overnightCrew', 'overnightAccess',
                  'noiseOrdinance', 'timeCutOff', 'fkRegionCode', 'fkMicroRegionCode', 'coordinates', 'active',
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
    detail = forms.CharField()
    requestingContact = forms.CharField(required=True)
    priority = forms.CharField(required=True)
    statusCode = forms.CharField(required=True, max_length=30)

    dateCompleted = forms.DateField(required=True)
    inspectForStorePath = forms.FileField(required=False, allow_empty_file=True,
                                          validators=[FileExtensionValidator(['pdf', 'txt'])])
    detailedReceiptPath = forms.FileField(required=False, allow_empty_file=True,
                                          validators=[FileExtensionValidator(['pdf', 'txt'])])
    signageMapPath = forms.FileField(required=False, allow_empty_file=True,
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

    model = WorkOrderStatus
    fields = 'status'


class ScopeOfWorkForm(BaseForm):
    GB_Counter = forms.IntegerField(min_value=0)
    GB_CounterBillable = forms.IntegerField(min_value=0)
    SOWPicturePath = forms.ImageField(required=True)
    WrongLocation = forms.BooleanField()
    ConcretePatchNeeded = forms.BooleanField()
    fkRightSOWID = forms.CharField(required=True)
    fkStatusID = forms.CharField(required=True)
    completedPicturePath = forms.ImageField(required=False)
    dateFieldEditedStatus = forms.DateField()
    timeFieldEditedStatus = forms.DateTimeField()
    approvedBilling = forms.BooleanField()
    fkInstallerID = forms.CharField(required=True)
    fkRequireMaterials = forms.CharField(required=True)
    fkLocationInStoreID = forms.CharField(required=True)
    fkWorkOrderID = forms.CharField(required=True)
    fkInitialLaborID = forms.CharField(required=True)
    fkExtraLaborID = forms.CharField(required=True)
    fkCorrectLaborID = forms.CharField(required=True)

    model = ScopeOfWork
    fields = ('GB_Counter', 'GB_CounterBillable', 'SOWPicturePath', 'WrongLocation', 'ConcretePatchNeeded', 'fkRightSOWID', 'fkStatusID', 'completedPicturePath', 'dateFieldEditedStatus', 'timeFieldEditedStatus', 'approvedBilling', 'fkInstallerID', 'fkRequireMaterials', 'fkLocationInStoreID', 'fkWorkOrderID', 'fkInitialLaborID', 'fkExtraLaborID', 'fkCorrectLaborID')


class ScopeOfWorkStatusForm(BaseForm):
    status = forms.CharField(required=True, max_length=50)

    model = ScopeOfWorkStatus
    fields = 'status'


class LaborItemForm(BaseForm):
    quantity = forms.IntegerField(min_value=1)
    fkArticleNumberState = forms.CharField(required=True)

    model = LaborItem
    fields = ('quantity', 'fkArticleNumberState')


class ArticleNumberStateForm(BaseForm):
    state = forms.CharField(max_length=2, min_length=2, required=True)
    price = forms.DecimalField(required=True, decimal_places=2)
    fkArticleNumber = forms.CharField(required=True)

    model = ArticleNumberState
    fields = ('state', 'price', 'fkArticleNumber',)


class ArticleNumberForm(BaseForm):
    articleNumber = forms.CharField()
    description = forms.CharField()  # Make this a list of Strings
    usedByInspectionCompanyButNotPrSkate = forms.BooleanField()
    capital = forms.BooleanField()

    model = ArticleNumber
    fields = ('articleNumber', 'description', 'usedByInspectionCompanyButNotPrSkate', 'capital')


class MaterialItemForm(BaseForm):
    materialArticleNumber = forms.CharField(required=True)
    description = forms.CharField()  # Make this a list of Strings

    model = MaterialItem
    fields = ('materialArticleNumber', 'description')


class MaterialListForm(BaseForm):
    fkMaterialItem = forms.CharField()  # Make a list of references (forms should be a list of Char fields)

    model = MaterialList
    fields = 'fkMaterialItem'


class LocationInStoreForm(BaseForm):
    department = forms.CharField(required=True)  # Should be unique with aisle, bay, tower, fkStoreNumber
    aisle = forms.CharField(required=True)
    bay = forms.CharField(required=True)
    tower = forms.CharField(required=True)
    level = forms.CharField(required=True)
    plumbingInLocation = forms.BooleanField()
    plumbingPicturePath = forms.ImageField()
    plumbingPicturePath2 = forms.ImageField()
    electricalInLocation = forms.BooleanField()
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
    downloadMLX = forms.BooleanField()
    excelInspectUploaded = forms.BooleanField()
    inspectionPictures = forms.BooleanField()
    postedSync = forms.BooleanField()
    formComplete = forms.BooleanField()
    concretePatchNeeded = forms.BooleanField()
    materialOrderNumberHD = forms.CharField()
    cpn_eta = forms.DateTimeField()
    inspectionDueDates = forms.DateTimeField()
    lastDateChecked = forms.DateTimeField()
    fkWorkOrderName = forms.CharField(required=True)

    model = PrepWork
    fields = (
        'downloadMLX', 'excelInspectUploaded', 'inspectionPictures', 'postedSync', 'formComplete',
        'concretePatchNeeded',
        'materialOrderNumberHD', 'cpn_eta', 'inspectionDueDates', 'lastDateChecked', 'fkWorkOrderName')
