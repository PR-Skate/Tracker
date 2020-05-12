# Created By: Alex Peterson
# Created On: 05/07/2020
#

from Class_Types.base_record import BaseRecord
from mongoengine import StringField


class RegionCode(BaseRecord):
    regionCodeID = StringField(max_length=12, required=True, unique=True)
    name = StringField(max_length=50, required=True, unique=True)
    meta = {'collection': 'RegionCode'}
