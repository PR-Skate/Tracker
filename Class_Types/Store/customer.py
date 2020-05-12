# Created By: Alex Peterson
# Created On: 05/07/2020
#
from mongoengine import StringField, DateTimeField, EmailField, DecimalField, BooleanField, \
    EmbeddedDocumentField, Document, ReferenceField
from Class_Types.base_record import BaseRecord
import re
import re

class Customer(BaseRecord):
    customerName = StringField(max_length=50, required=True, unique=True)
    meta = {'collection': 'Customer'}