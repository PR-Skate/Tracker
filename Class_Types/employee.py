# Created By: Alex Peterson
# Created On: 05/11/2020
#
import re

import bcrypt as bcrypt
from mongoengine import StringField, EmailField, DecimalField, BooleanField, \
    EmbeddedDocumentField, DynamicField, DateField
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
    _passwordHashBytes = DynamicField(required=True, db_field='passwordHash')
    type = StringField(max_length=10, required=True)
    meta = {'collection': 'Employee'}

    @property
    def passwordHash(self):
        return self._passwordHashBytes

    @passwordHash.setter
    def passwordHash(self, passwordString):
        self._passwordHashBytes = bcrypt.hashpw(passwordString.encode('utf-8'), bcrypt.gensalt(12))

    def validatePassword(self, passwordVerify):
        return bcrypt.checkpw(passwordVerify.encode('utf-8'), self._passwordHashBytes)
