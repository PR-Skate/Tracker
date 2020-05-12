# Created By: Alex Peterson
# Created On: 05/07/2020
#

from mongoengine import StringField, DateTimeField, EmailField, DecimalField, BooleanField, EmbeddedDocumentField, Document
from Tracker.Class_Types.base_record import BaseRecord
import re


class RegionCode(BaseRecord):
    regionCodeID = StringField(max_length=12, required=True, unique=True)
    name = StringField(max_length=50, required=True, unique=True)
    meta = {'collection': 'RegionCode'}