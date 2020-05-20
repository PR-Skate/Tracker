import re
from mongoengine import StringField, DynamicEmbeddedDocument, EmbeddedDocument


class Address(EmbeddedDocument):
    addressLineOne = StringField(max_length=150, required=True)
    addressLineTwo = StringField(max_length=150, required=False, allow_null=True, allow_blank=True, blank=True, null=True)
    city = StringField(max_length=75, required=True)
    state = StringField(max_length=2, required=True)
    zip = StringField(regex=re.compile('^\d{5}'), max_length=5, required=True)
    country = StringField(max_length=75, required=True)

    @classmethod
    def get_optional_fields(cls):
        temp = list()
        for field, object in cls._fields.items():
            if not object.__getattribute__('required'):
                temp.append(object.__getattribute__('db_field'))
        if '_id' in temp:
            temp.remove('_id')
        if '_cls' in temp:
            temp.remove('_cls')
        return temp

    @classmethod
    def get_fields(cls):
        temp = list(cls._db_field_map.values())
        if '_id' in temp:
            temp.remove('_id')
        if '_cls' in temp:
            temp.remove('_cls')
        return temp

class Name(DynamicEmbeddedDocument):
    _firstName = StringField(max_length=150, required=True, db_field='firstName')
    _lastName = StringField(max_length=150, default='', db_field='lastName')
    fullName = StringField(max_length=300, required=True)

    @property
    def firstName(self):
        print('firstName: Get')
        return self._firstName

    @firstName.setter
    def firstName(self, value):
        print('firstName: Set')
        self._firstName = value
        if self.lastName:
            self.fullName = self._firstName + ' ' + self.lastName

    @property
    def lastName(self):
        print('lastName: Get')
        return self._lastName

    @lastName.setter
    def lastName(self, value):
        print('lastName: Set')
        self._lastName = value
        if self.firstName:
            self.fullName = self.firstName + ' ' + self._lastName

    @classmethod
    def get_optional_fields(cls):
        temp = list()
        for field, object in cls._fields.items():
            if not object.__getattribute__('required'):
                temp.append(object.__getattribute__('db_field'))
        if '_id' in temp:
            temp.remove('_id')
        if '_cls' in temp:
            temp.remove('_cls')
        return temp