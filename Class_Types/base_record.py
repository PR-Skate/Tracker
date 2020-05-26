# Created By: Chase Crossley
# Created On: 05/11/2020

from datetime import datetime

import bson as bson
from mongoengine import DateTimeField, DynamicDocument, ReferenceField, ValidationError


class BaseRecord(DynamicDocument):
    _createdUser = ReferenceField('Employee', required=True, db_field='createdUser', dbref=True)
    createdTimestamp = DateTimeField(default=datetime.now(), required=False)
    _lastModifiedUser = ReferenceField('Employee', db_field='lastModifiedUser', dbref=True, required=False, blank=True,
                                       null=True)
    lastModifiedTimestamp = DateTimeField(default=datetime.now(), required=False)
    meta = {'allow_inheritance': True, 'abstract': True}

    @property
    def createdUser(self):
        return self._createdUser

    @createdUser.setter
    def createdUser(self, value):
        if isinstance(value, bson.DBRef):
            pass
        elif not isinstance(value, bson.ObjectId):
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
            value = bson.ObjectId(value)
            self._lastModifiedUser = value

    @classmethod
    def get_fields(cls):
        temp = list(cls._db_field_map.values())
        if '_id' in temp:
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

    def is_valid_reference_field(self, field):
        if self._data.get(field):
            object_id = bson.ObjectId(
                self._data.get(field) if isinstance(self._data.get(field), bson.ObjectId) else self._data.get(
                    field).id)
            model = object.__getattribute__('document_type')
            if model == 'self':
                model = self.__class__
            try:
                model.objects.get(id=object_id)
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

    def save(self, force_insert=False, validate=True, clean=True, write_concern=None, cascade=None, cascade_kwargs=None,
             _refs=None, save_condition=None, signal_kwargs=None, **kwargs):
        try:
            self.custom_validate()
            return DynamicDocument.save(self, force_insert, validate, clean, write_concern, cascade, cascade_kwargs,
                                        _refs, save_condition, signal_kwargs, **kwargs)
        except Exception as e:
            print(e)

    def is_field_unique(self, field):
        field_value = {field: self._data.get(field)}
        return self.__class__.objects(**field_value).count() < 1

    def update(self, **kwargs):
        for field, value in kwargs.items():
            self.__setattr__(field, value)
        return self.save()
