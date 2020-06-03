import re

from mongoengine import StringField, DynamicEmbeddedDocument, EmbeddedDocument, DecimalField


class Coordinates(DynamicEmbeddedDocument):
    longitude = DecimalField(min_value=-180, max_value=180, precision=25)
    latitude = DecimalField(min_value=-90, max_value=90, precision=25)



class Address(EmbeddedDocument):
    addressLineOne = StringField(max_length=150, required=True)
    addressLineTwo = StringField(max_length=150, required=False, allow_null=True, allow_blank=True, blank=True,
                                 null=True)
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

    def __str__(self):
        return '{addressLineOne}' \
               '{addressLineTwo}\n' \
               '{city}, {state} {zip}\n' \
               '{country}'.format(
            addressLineOne=self.addressLineOne,
            addressLineTwo='\n' + self.addressLineTwo if self.addressLineTwo else '',
            city=self.city, state=self.state,
            zip=self.zip, country=self.country)


class Name(DynamicEmbeddedDocument):
    _firstName = StringField(max_length=150, required=True, db_field='firstName')
    _lastName = StringField(max_length=150, default='', db_field='lastName')
    fullName = StringField(max_length=300, required=True)

    @property
    def firstName(self):
        return self._firstName

    @firstName.setter
    def firstName(self, value):
        self._firstName = value.strip()
        if self.lastName:
            self.fullName = self._firstName + ' ' + self.lastName
            self.fullName = self.fullName.strip()

    @property
    def lastName(self):
        return self._lastName

    @lastName.setter
    def lastName(self, value):
        self._lastName = value.strip()
        if self.firstName:
            self.fullName = self.firstName + ' ' + self._lastName
            self.fullName = self.fullName.strip()

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

    def __str__(self):
        return str(self.lastName + '\n' + self.firstName).strip()