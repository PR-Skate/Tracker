# Created By: Alex Peterson     Petersonalex99@gmail.com
# Created On: 05/07/2020
#

from mongoengine import StringField, BooleanField, \
    EmbeddedDocumentField, ReferenceField, EmailField, DateField, \
    ListField, IntField

from ..Embeded_Documents.embeded_classes import Address, Name, Coordinates
from ..base_record import BaseRecord


class Store(BaseRecord):
    OPTIONS = (
        ('SUN', 'Sunday'),
        ('MON', 'Monday'),
        ('TUES', 'Tuesday'),
        ('WED', 'Wednesday'),
        ('THURS', 'Thursday'),
        ('FRI', 'Friday'),
        ('SAT', 'Saturday')
    )

    # constructor:
    storeNumber = StringField(max_length=50, required=True)
    fkCustomer = ReferenceField('Customer', required=True, dbref=False)
    address = EmbeddedDocumentField(Address, required=True)
    phoneNumber = StringField(max_length=20, required=True)
    region = StringField(max_length=50, required=True)

    division = StringField(max_length=50, required=True)
    awardedVendor = StringField(max_length=50, required=True, default='PR Skate')

    overnightCrew = StringField(max_length=25)  # choices: Full Time or Part Time

    overnightAccess = ListField(StringField(max_length=5), choices=(
        ('SUN', 'Sunday'),
        ('MON', 'Monday'),
        ('TUES', 'Tuesday'),
        ('WED', 'Wednesday'),
        ('THURS', 'Thursday'),
        ('FRI', 'Friday'),
        ('SAT', 'Saturday')
    ))
    noiseOrdinance = BooleanField(default=False)
    timeCutOff = StringField()

    fkRegionCode = ReferenceField('RegionCode', dbref=False)
    fkMicroRegionCode = ReferenceField('MicroRegionCode', dbref=False)
    coordinates = EmbeddedDocumentField(Coordinates)
    active = BooleanField(default=False)
    installationDueDates = ListField(DateField())  # Uploaded able
    inspectionDueDates = ListField(DateField())  # Uploaded able MAYBE NEW TABLES
    fiscalWeek = IntField(min_value=1, max_value=53)

    storeManagerName = EmbeddedDocumentField(Name)
    storeManagerEmail = EmailField()

    opsManagerName = EmbeddedDocumentField(Name)
    opsManagerEmail = EmailField()
    managerName = EmbeddedDocumentField(Name)
    managerEmail = EmailField()
    overnightManagerName = EmbeddedDocumentField(Name)
    overnightManagerEmail = EmailField()

    meta = {'collection': 'Store'}

    def __str__(self):
        return f'{self.storeNumber} - {self.address.city} - {self.address.state}'
