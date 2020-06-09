import copy
import re

from mongoengine import StringField, DynamicEmbeddedDocument, DecimalField, ReferenceField, \
    EmbeddedDocumentField, ListField


def display_string(string):
    words = list()
    word = ''
    for letter in string:
        if letter.islower():
            if not word:
                letter = letter.upper()
            word += letter
        else:
            words.append(word)
            word = letter
    words.append(word)
    return ' '.join(words)


def camel_case_to_upper(string):
    return ''.join(display_string(string).split(' '))


class BaseEmbeddedDocument(DynamicEmbeddedDocument):
    meta = {'allow_inheritance': True, 'abstract': True}

    @classmethod
    def get_form_fields_items(cls):
        return cls._fields.items()

    @classmethod
    def get_field_information(cls, main_field_name):

        class FieldInformation(object):
            name = None
            model_name = None
            model = None
            filter = None
            type = None
            list_field_information = None
            list_choices = None
            sub_form_fields_information = None
            required = None

            def __str__(self):
                return f'{self.model_name}'

        field_information_list = list()
        for field_name, field_class in cls.get_form_fields_items():
            field_name = field_name.strip('_')
            if field_name != 'cls':
                field_information = FieldInformation()
                field_information.model_name = field_name
                field_information.name = display_string(field_name)
                field_information.type = field_class.__class__.__name__
                field_information.required = field_class.__getattribute__('required')
                if isinstance(field_class, ListField):
                    field_information.list_field_type = field_class.__getattribute__('field').__class__.__name__
                    if hasattr(field_class.field, 'choices'):
                        field_information.list_choices = field_class.__getattribute__('choices')
                elif isinstance(field_class, ReferenceField) or isinstance(field_class, EmbeddedDocumentField):
                    field_information.model = field_class.__getattribute__('document_type')
                    if not isinstance(field_information.model, str):
                        if isinstance(field_class, EmbeddedDocumentField):
                            field_information.sub_form_fields_information = field_information.model.get_field_information(
                                field_name)
                        field_information.model = field_information.model.__name__
                    else:
                        if field_information.model == 'self':
                            field_information.model = cls.__name__
                field_information_list.append(field_information)
        return field_information_list


class Coordinates(BaseEmbeddedDocument):
    longitude = DecimalField(min_value=-180, max_value=180, precision=25)
    latitude = DecimalField(min_value=-90, max_value=90, precision=25)

    def __str__(self):
        return f'{self.latitude}, {self.longitude}'


class Address(BaseEmbeddedDocument):
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


class Name(BaseEmbeddedDocument):
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

    @classmethod
    def get_form_fields_items(cls):
        temp = copy.deepcopy(cls._fields)
        temp.pop('fullName')
        return temp.items()

    def __str__(self):
        return str(self.lastName + '\n' + self.firstName).strip()
