# Created By: Alex Peterson     Petersonalex99@gmail.com
# Created On: 05/07/2020
#

from mongoengine import StringField, DateTimeField, EmailField, DecimalField, BooleanField, \
    EmbeddedDocumentField, Document

from Class_Types.base_record import BaseRecord
from Class_Types.Embeded_Documents.embeded_classes import Address
import re

class WorkOrderStatus(BaseRecord):
    # constructor:
    workOrderStatusID = StringField(unique=True, max_length=30)
    name = StringField(max_length=75)
    meta = {'collection': 'WorkOrderStatus'}