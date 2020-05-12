# Created By: Alex Peterson
# Created On: 05/11/2020
#
from mongoengine import StringField, DateTimeField, EmailField, DecimalField, BooleanField, \
    EmbeddedDocumentField

from Class_Types.base_record import BaseRecord
from Class_Types.Embeded_Documents.embeded_classes import Address
import re


class Employee(BaseRecord):
    userName = StringField(max_length=50, required=True, unique=True)
    firstName = StringField(max_length=50, required=True)
    lastName = StringField(max_length=50, required=True)
    birthDate = DateTimeField(required=True)
    address = EmbeddedDocumentField(Address, required=True)
    email = EmailField(required=True, unique=True)
    phone = StringField(max_length=20, required=True)
    pin = StringField(regex=re.compile('^\d{4}'), max_length=4, required=True)
    rateOfPay = DecimalField()
    active = BooleanField(required=True)
    password = StringField(max_length=256, required=True)
    type = StringField(max_length=10, required=True)
    meta = {'collection': 'Employee'}
