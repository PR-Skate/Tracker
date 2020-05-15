# Created By: Alex Peterson
# Created On: 05/11/2020
#
import bcrypt as bcrypt
from mongoengine import StringField, DateTimeField, EmailField, DecimalField, BooleanField, \
    EmbeddedDocumentField, DynamicField

from Class_Types.base_record import BaseRecord
from Class_Types.Embeded_Documents.embeded_classes import Address
import re
import hashlib
import os



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
    active = BooleanField(default=False)
    _passwordHashBytes = DynamicField(required=True, db_field='passwordHash')
    type = StringField(max_length=10, required=True)
    meta = {'collection': 'Employee'}

    @property
    def passwordHash(self):
        return self._passwordHashBytes

    @passwordHash.setter
    def passwordHash(self, passwordString):
        self._passwordHashBytes = bcrypt.hashpw(passwordString.encode('utf-8'), bcrypt.gensalt( 12 ))

    def validatePassword(self, passwordVerify):
        return bcrypt.checkpw(passwordVerify.encode('utf-8'), self._passwordHashBytes)
