# Created By: Alex Peterson     Petersonalex99@gmail.com
# Created On: 05/07/2020
#

import datetime as dt

from mongoengine import DateField, StringField, FileField, ReferenceField

from Class_Types.base_record import BaseRecord


class WorkOrder(BaseRecord):
    # constructor:
    workOrderName = StringField(max_length=15, required=True, unique=True)
    dateReceived = DateField(required=True, default=dt.datetime.now())
    detail = StringField(defualt='', required=True)
    requestingContact = StringField(required=True)
    statusCode = StringField(max_length=30, required=True)

    dateCompleted = DateField(required=True)
    inspectForStorePath = FileField()
    detailedReceiptPath = FileField()
    signageMapPath = FileField()
    partsArrivalDate = DateField()

    targetStartDate = DateField(required=True)
    fkWorkOrderStatus = ReferenceField('WorkOrderStatus', required=True)
    fkStoreNumber = ReferenceField('Store', required=True)
    meta = {'collection': 'WorkOrder'}
