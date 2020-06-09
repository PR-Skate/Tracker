from mongoengine import StringField

from Class_Types.base_record import BaseRecord


class MicroRegionCode(BaseRecord):
    microRegionCode = StringField(max_length=12, required=True, unique=True, db_field='regionCode')
    meta = {'collection': 'MicroRegionCode'}

    def __str__(self):
        return self.microRegionCode
