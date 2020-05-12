# Created By: Alex Peterson     Petersonalex99@gmail.com
# Created On: 05/07/2020
#

import time as t
from mongoengine import StringField, DateTimeField, EmailField, DecimalField, BooleanField, \
    EmbeddedDocumentField, Document, ReferenceField, EmailField, SortedListField, PointField, DateField, \
    ListField, IntField

from Class_Types.base_record import BaseRecord
from Class_Types.Embeded_Documents.embeded_classes import Address
from Class_Types.Embeded_Documents.embeded_classes import Name
import re


class Store(BaseRecord):
    # constructor:
    storeNumber = StringField(max_length=50, required=True)
    fkCustomer = ReferenceField('Customer')
    address = EmbeddedDocumentField(Address, required=True)
    phoneNumber = StringField(max_length=20, required=True)
    region = StringField(max_length=50, required=True)
    
    division = StringField(max_length=50, required=True)
    awardedVendor = StringField(max_length=50, required=True, default='PR Skate')
    storeManagerName = EmbeddedDocumentField(Name, required=True)
    storeManagerEmail = EmailField()

    opsManagerName = EmbeddedDocumentField(Name, required=True)
    opsManagerEmail = EmailField()
    managerName = EmbeddedDocumentField(Name, required=True)
    managerEmail = EmailField()
    overnightManagerName = EmbeddedDocumentField(Name, required=True)

    overnightManagerEmail = EmailField()
    overnightCrew = StringField(max_length=25, required=True)
    overnightAccess = SortedListField()
    noiseOrdinance = BooleanField(default=False, required=True)
    timeCuttOff = DateTimeField(required=True)

    fkRegionCode = ReferenceField('RegionCode')
    fkMicroRegionCode = ReferenceField('MicroRegionCode')
    cordinated= PointField()
    active = BooleanField(default=True)
    installationDueDates = ListField(DateField)
    fiscalWeek = IntField(min_value=1, max_value=53)
    meta = {'collection': 'Store'}