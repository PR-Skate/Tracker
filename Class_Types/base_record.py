# Created By: Chase Crossley
# Created On: 05/11/2020

from datetime import datetime

import bson as bson
from mongoengine import DateTimeField, DynamicDocument, ReferenceField, ValidationError, EmbeddedDocumentField, \
    ListField

from PR_Skate.logging import log_methods


# @log_methods
class BaseRecord(DynamicDocument):
    _createdUser = ReferenceField('Employee', required=True, db_field='createdUser', dbref=True)
    createdTimestamp = DateTimeField(default=datetime.now(), required=False)
    _lastModifiedUser = ReferenceField('Employee', db_field='lastModifiedUser', dbref=True, required=False, blank=True,
                                       null=True)
    lastModifiedTimestamp = DateTimeField(default=datetime.now(), required=False)
    meta = {'allow_inheritance': True, 'abstract': True}

    def __init_subclass__(cls, **kwargs):
        return log_methods(cls=cls)

    @property
    def createdUser(self):
        return self._createdUser

    @createdUser.setter
    def createdUser(self, value):
        if isinstance(value, bson.DBRef):
            pass
        elif bson.ObjectId.is_valid(value):
            value = bson.ObjectId(value)
        else:
            from Class_Types import Employee
            value = Employee.objects.get(userName=value).id
        if not self.lastModifiedUser:
            self.lastModifiedUser = value
        self._createdUser = value

    @property
    def lastModifiedUser(self):
        return self._lastModifiedUser

    @lastModifiedUser.setter
    def lastModifiedUser(self, value):
        if value:
            if isinstance(value, bson.DBRef):
                pass
            elif bson.ObjectId.is_valid(value):
                value = bson.ObjectId(value)
            else:
                from Class_Types import Employee
                value = Employee.objects.get(userName=value).id
            self._lastModifiedUser = value

    @classmethod
    def get_all_fields(cls):
        return list([x.strip('_') for x in cls._db_field_map.values()])

    @classmethod
    def get_fields(cls, get_id=False):
        temp = list(cls._db_field_map.values())
        if '_id' in temp and not get_id:
            temp.remove('_id')

        if '_cls' in temp:
            temp.remove('_cls')
        return temp

    @classmethod
    def get_required_fields(cls):
        temp = list()
        if not cls._meta.get('abstract'):
            for field, object in cls._fields.items():
                if object.__getattribute__('required'):
                    temp.append(object.__getattribute__('db_field'))
        if '_id' in temp:
            temp.remove('id')
        if '_cls' in temp:
            temp.remove('_cls')
        return temp

    @classmethod
    def get_optional_fields(cls):
        temp = list()
        if not cls._meta.get('abstract'):
            for field, object in cls._fields.items():
                if not object.__getattribute__('required'):
                    temp.append(object.__getattribute__('db_field'))
        if '_id' in temp:
            temp.remove('_id')
        if '_cls' in temp:
            temp.remove('_cls')
        return temp

    @classmethod
    def get_reference_fields(cls):
        temp = list()
        if not cls._meta.get('abstract'):
            for field, object in cls._fields.items():
                if isinstance(object, ReferenceField) and field != '_lastModifiedUser' and field != '_createdUser':
                    temp.append(object.__getattribute__('db_field'))
        if '_id' in temp:
            temp.remove('_id')
        if '_cls' in temp:
            temp.remove('_cls')
        return temp

    @staticmethod
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

    @classmethod
    def get_field_information(cls):

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
            hidden = None

            def __str__(self):
                return f'{self.model_name}'

        field_information_list = list()
        base_record_fields = BaseRecord.get_all_fields()
        for field_name, field_class in cls._fields.items():
            field_name = field_name.strip('_')
            field_information = FieldInformation()
            field_information.model_name = field_name
            field_information.name = cls.display_string(field_name)
            field_information.type = field_class.__class__.__name__
            field_information.required = field_class.__getattribute__('required')
            if field_name == 'id' or field_name in base_record_fields:
                field_information.hidden = True
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

    def is_valid_reference_field(self, field):
        if self._data.get(field):
            if not isinstance(self._data.get(field), bson.ObjectId):
                object_id = bson.ObjectId(
                    self._data.get(field) if bson.ObjectId.is_valid(self._data.get(field))
                    else self._data.get(field).id)
            else:
                object_id = self._data.get(field)
            model = self._fields.get(field).__getattribute__('document_type')
            if model == 'self':
                model = self.__class__
            try:
                model.objects.get(id=object_id)
                setattr(self, field, object_id)
                return True
            except model.DoesNotExist:
                pass
            return False

    def custom_validate(self):
        errors = {}
        for field, object_field in self._fields.items():
            if isinstance(object_field, ReferenceField) and not self.is_valid_reference_field(field):
                if field in errors.keys():
                    if not field in errors.keys():
                        errors.update({field: ['ReferenceError']})
                    else:
                        errors.get(field).append('ReferenceError')

            if object_field.__getattribute__('unique') and not self.is_field_unique(field):
                if not field in errors.keys():
                    errors.update({field: ['DuplicateKeyError']})
                else:
                    errors.get(field).append('DuplicateKeyError')
        if errors:
            raise ValidationError('There was errors with the following field(s)', errors=errors)

    def get_form_data(self):
        data = dict()
        for key, value in self._data.items():
            key = key.strip('_')
            data.update({key: value})
        return data

    def save(self, force_insert=False, validate=True, clean=True, write_concern=None, cascade=None, cascade_kwargs=None,
             _refs=None, save_condition=None, signal_kwargs=None, **kwargs):
        try:
            self.custom_validate()
            return DynamicDocument.save(self, force_insert, validate, clean, write_concern, cascade, cascade_kwargs,
                                        _refs, save_condition, signal_kwargs, **kwargs)
        except Exception as e:
            raise e

    def is_field_unique(self, field):
        field_value = {field: self._data.get(field)}
        return self.__class__.objects(**field_value).count() < 1

    def update(self, **kwargs):
        for field, value in kwargs.items():
            self.__setattr__(field, value)

        return self.save()
