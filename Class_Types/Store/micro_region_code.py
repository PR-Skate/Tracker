from mongoengine import StringField, DateTimeField, EmailField, DecimalField, BooleanField, \
    EmbeddedDocumentField, Document

from Class_Types.base_record import BaseRecord
from Class_Types.Embeded_Documents.embeded_classes import Address
import re



class MicroRegionCode(BaseRecord):
    regionCode = StringField(max_length=12, required=True, unique=True)
    name = StringField(max_length=50, required=True, unique=True)
    meta = {'collection': 'MicroRegionCode'}