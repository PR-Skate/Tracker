# Created By: Chase Crossley
# Created On: 05/11/2020

from datetime import datetime
from mongoengine import connect, Document, StringField, DateTimeField, FieldDoesNotExist, DynamicDocument
import json
import inspect


class BaseRecord(DynamicDocument):
    _createdUser = StringField(max_length=50, required=True, db_field='createdUser') #TODO: MAKE REFFERENCE
    createdTimestamp = DateTimeField(default=datetime.now())
    lastModifiedUser = StringField(max_length=50)
    lastModifiedTimestamp = DateTimeField(default=datetime.now())
    connection = connect(
        host='mongodb://root:6iskvVzSpjcGjOcB8Qfm7htg1@138.68.22.230:27017/Tracker?authSource=admin&readPreference=primary&appname=MongoDB%20Compass&ssl=false')
    meta = {'allow_inheritance': True, 'abstract': True}


    @property
    def createdUser(self):
        print('hi')
        return self._createdUser

    @createdUser.setter
    def createdUser(self, value):
        print('bye')
        if not self.lastModifiedUser:
            self.lastModifiedUser = value
        self._createdUser = value

    @classmethod
    def get_fields(cls):
        temp = list(cls._db_field_map.values())
        temp.remove('_id')
        return temp
