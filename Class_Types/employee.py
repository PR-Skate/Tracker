# Created By: Alex Peterson
# Created On: 05/11/2020
#
from mongoengine import StringField, DateTimeField, EmailField, DecimalField, BooleanField, \
    EmbeddedDocumentField

from Class_Types.base_record import BaseRecord
from Class_Types.Embeded_Documents.embeded_classes import Address
import re
import hashlib


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
    _passwordHash = StringField(max_length=256, required=True, db_field='passwordHash')
    type = StringField(max_length=10, required=True)
    meta = {'collection': 'Employee'}

    @property
    def passwordHash(self):
        return self._passwordHash

    @passwordHash.setter
    def passwordHash(self, passwordString):
        self._passwordHash = hashlib.pbkdf2_hmac(
            'sha256',  # The hash digest algorithm for HMAC
            passwordString.encode('utf-8'),  # Convert the password to bytes
            100000,  # It is recommended to use at least 100,000 iterations of SHA-256
            dklen=128
        )

    def validatePassword(self, passwordVerify):
        newKey = hashlib.pbkdf2_hmac(
            'sha256',  # The hash digest algorithm for HMAC
            passwordVerify.encode('utf-8'),  # Convert the password to bytes
            100000,  # It is recommended to use at least 100,000 iterations of SHA-256
            dklen=128
        )

        return newKey == self._passwordHash
