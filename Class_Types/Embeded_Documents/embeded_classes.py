import re
from mongoengine import StringField, EmbeddedDocument


class Address(EmbeddedDocument):
    addressLineOne = StringField(max_length=150, required=True)
    addressLineTwo = StringField(max_length=150)
    city = StringField(max_length=75, required=True)
    state = StringField(max_length=2, required=True)
    zip = StringField(regex=re.compile('^\d{5}'), max_length=5, required=True)
    country = StringField(max_length=75, required=True)


class Name(EmbeddedDocument):
    _firstName = StringField(max_length=150, required=True, db_field='firstName')
    _lastName = StringField(max_length=150, default='', db_field='lastName')
    fullName = StringField(max_length=300, required=True)


    @property
    def firstName(self):
        return self._firstName

    @firstName.setter
    def firstName(self, value):
        self._firstName = value
        self.fullName = self._firstName + ' ' + self._lastName

    @property
    def lastName(self):
        return self._lastName

    @lastName.setter
    def lastName(self, value):
        self._lastName = value
        self.fullName = self._firstName + ' ' + self._lastName
