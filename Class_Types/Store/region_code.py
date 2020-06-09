# Created By: Alex Peterson
# Created On: 05/07/2020
#

from mongoengine import StringField

from Class_Types.base_record import BaseRecord


class RegionCode(BaseRecord):
    regionCode = StringField(max_length=12, required=True, unique=True)
    meta = {'collection': 'RegionCode'}

    def __str__(self):
        return self.regionCode
