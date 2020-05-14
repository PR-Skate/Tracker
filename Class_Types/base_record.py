# Created By: Chase Crossley
# Created On: 05/11/2020

from datetime import datetime

from mongoengine import connect, StringField, DateTimeField, DynamicDocument


class BaseRecord(DynamicDocument):
    _createdUser = StringField(max_length=50, required=True, db_field='createdUser')  # TODO: MAKE REFFERENCE
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
        temp.remove('_cls')
        return temp

    @classmethod
    def get_optional_fields(cls):
        temp = list()
        if not cls._meta.get('abstract'):
            for field, object in cls._fields.items():
                if not object.__getattribute__('required'):
                    # temp.append()
                    temp.append(field)
        temp.remove('id')
        temp.remove('_cls')
        return temp