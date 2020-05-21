# Created By: Chase Crossley
# Created On: 05/11/2020

from datetime import datetime

import bson as bson
from mongoengine import connect, DateTimeField, DynamicDocument, ReferenceField


class BaseRecord(DynamicDocument):
    _createdUser = ReferenceField('Employee', required=True, db_field='createdUser', dbref=True)
    createdTimestamp = DateTimeField(default=datetime.now(), required=False)
    _lastModifiedUser = ReferenceField('Employee', db_field='lastModifiedUser', dbref=True, required=False,
                                       allow_null=True, allow_blank=True, blank=True, null=True)
    lastModifiedTimestamp = DateTimeField(default=datetime.now(), required=False)
    connection = connect(
        host='mongodb://root:6iskvVzSpjcGjOcB8Qfm7htg1@138.68.22.230:27017/Tracker?authSource=admin&readPreference=primary&appname=MongoDB%20Compass&ssl=false')
    meta = {'allow_inheritance': True, 'abstract': True}

    @property
    def createdUser(self):
        return self._createdUser

    @createdUser.setter
    def createdUser(self, value):
        value = bson.ObjectId(value)
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

    def validate_reference_fields(self):
        not_properly_referenced = list()
        for field, object in self._fields.items():
            if self._data.get(field) and isinstance(object, ReferenceField):
                object_id = bson.ObjectId(self._data.get(field))
                model = object.__getattribute__('document_type')
                if model == 'self':
                    model = self.__class__
                try:
                    model.objects.get(id=object_id)
                    continue
                except model.DoesNotExist:
                    not_properly_referenced.append(self._db_field_map.get(field))
        return not_properly_referenced

    def save(self, force_insert=False, validate=True, clean=True, write_concern=None, cascade=None, cascade_kwargs=None,
             _refs=None, save_condition=None, signal_kwargs=None, **kwargs):
        not_properly_referenced = self.validate_reference_fields()
        if len(not_properly_referenced) == 0:
            return DynamicDocument.save(self, force_insert, validate, clean, write_concern, cascade, cascade_kwargs,
                                        _refs, save_condition, signal_kwargs, **kwargs)
        else:
            raise Exception('Reference Fields do not have correct references: ' + ' '.join(not_properly_referenced))
