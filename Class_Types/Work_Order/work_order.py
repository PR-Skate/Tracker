# Created By: Alex Peterson     Petersonalex99@gmail.com
# Created On: 05/07/2020
#

from mongoengine import StringField, DateTimeField, EmailField, DecimalField, BooleanField, \
    EmbeddedDocumentField, Document, DateField, StringField, FileField, ReferenceField

from Class_Types.base_record import BaseRecord
from Class_Types.Embeded_Documents.embeded_classes import Address
import re
import  datetime as dt
class WorkOrder(BaseRecord):
    # constructor:
    workOrderName = StringField(max_length=75, required = True)
    dateReceived = DateField(required=True, default=dt.datetime.now())
    detail = StringField(defualt='', required=True)
    requestingContact = StringField(required=True)
    statusCode = StringField(max_length=30, required=True)

    dateCompleted = DateField(required=True)
    inspectForStorePath = FileField()
    detailedReceiptPath = FileField()
    signageMapPath = FileField()
    partsArrivalDate = DateField(required=True)

    targetStartDate = DateField(required=True)
    fkWorkOrderStatus = ReferenceField('WorkOrderStatus')
    fkStoreNumber = ReferenceField('Store')
    meta = {'collection': 'WorkOrder'}