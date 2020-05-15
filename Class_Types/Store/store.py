# Created By: Alex Peterson     Petersonalex99@gmail.com
# Created On: 05/07/2020
#

from mongoengine import StringField, DateTimeField, BooleanField, \
    EmbeddedDocumentField, ReferenceField, EmailField, PointField, DateField, \
    ListField, IntField

from .micro_region_code import MicroRegionCode
from .region_code import RegionCode
from .customer import Customer
from ..Embeded_Documents.embeded_classes import Address, Name
from ..base_record import BaseRecord


class Store(BaseRecord):
    # constructor:
    storeNumber = StringField(max_length=50, required=True)
    fkCustomer = ReferenceField(Customer, required=True)
    address = EmbeddedDocumentField(Address, required=True)
    phoneNumber = StringField(max_length=20, required=True)
    region = StringField(max_length=50, required=True)

    division = StringField(max_length=50, required=True)
    awardedVendor = StringField(max_length=50, required=True, default='PR Skate')
    storeManagerName = EmbeddedDocumentField(Name)
    storeManagerEmail = EmailField()

    opsManagerName = EmbeddedDocumentField(Name)
    opsManagerEmail = EmailField()
    managerName = EmbeddedDocumentField(Name)
    managerEmail = EmailField()
    overnightManagerName = EmbeddedDocumentField(Name)

    overnightManagerEmail = EmailField()
    overnightCrew = StringField(max_length=25)
    overnightAccess = ListField(StringField())
    noiseOrdinance = BooleanField(default=False)
    timeCutOff = DateTimeField()

    fkRegionCode = ReferenceField(RegionCode)
    fkMicroRegionCode = ReferenceField(MicroRegionCode)
    coordinates = PointField()
    active = BooleanField(default=True)
    installationDueDates = ListField(DateField)
    inspectionDueDates = ListField(DateField)
    fiscalWeek = IntField(min_value=1, max_value=53)
    meta = {'collection': 'Store'}
