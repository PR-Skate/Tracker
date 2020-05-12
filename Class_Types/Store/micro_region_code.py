from mongoengine import StringField

from Class_Types.base_record import BaseRecord


class MicroRegionCode(BaseRecord):
    regionCode = StringField(max_length=12, required=True, unique=True)
    name = StringField(max_length=50, required=True, unique=True)
    meta = {'collection': 'MicroRegionCode'}
