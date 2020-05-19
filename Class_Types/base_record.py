# Created By: Chase Crossley
# Created On: 05/11/2020

from datetime import datetime

import bson as bson
from mongoengine import connect, DateTimeField, DynamicDocument, ReferenceField


class BaseRecord(DynamicDocument):
    _createdUser = ReferenceField('Employee', required=True, db_field='createdUser', dbref=True)  # TODO: MAKE REFFERENCE
    createdTimestamp = DateTimeField(default=datetime.now())
    _lastModifiedUser = ReferenceField('Employee', db_field='lastModifiedUser', dbref=True)
    lastModifiedTimestamp = DateTimeField(default=datetime.now())
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
