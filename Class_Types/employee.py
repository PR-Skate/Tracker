# Created By: Alex Peterson
# Created On: 05/11/2020
#
import re

from mongoengine import StringField, EmailField, DecimalField, BooleanField, \
    EmbeddedDocumentField, DateField

from Class_Types.Embeded_Documents.embeded_classes import Address, Name
from Class_Types.base_record import BaseRecord


class Employee(BaseRecord):
    userName = StringField(max_length=50, required=True, unique=True)
    name = EmbeddedDocumentField(Name, required=True)
    birthDate = DateField(required=True)
    address = EmbeddedDocumentField(Address, required=True)
    email = EmailField(required=True, unique=True)
    phone = StringField(max_length=20, required=True)
    pin = StringField(regex=re.compile('^\d{4}'), max_length=4, required=True)
    rateOfPay = DecimalField()
    active = BooleanField(default=False)
    durationMultiplier = DecimalField(min_value=0)
    type = StringField(max_length=10, required=True)
    meta = {'collection': 'Employee'}

    def __str__(self):
        return f'{self.userName} - {self.name}'
