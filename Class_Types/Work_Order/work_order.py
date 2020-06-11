# Created By: Alex Peterson     Petersonalex99@gmail.com
# Created On: 05/07/2020
#

import datetime as dt

from mongoengine import DateField, StringField, FileField, ReferenceField, GridFSProxy

from ..base_record import BaseRecord


class WorkOrder(BaseRecord):
    # constructor:
    workOrderName = StringField(max_length=15, required=True, unique=True)
    dateReceived = DateField(required=True, default=dt.datetime.now())
    detail = StringField(defualt='')
    requestingContact = StringField(required=True)
    priority = StringField(required=True)
    statusCode = StringField(max_length=30, required=True)

    dateCompleted = DateField(required=True)
    inspectForStoreFile = FileField()
    detailedReceiptFile = FileField()
    signageMapFile = FileField()
    partsArrivalDate = DateField()

    targetStartDate = DateField(required=True)
    fkWorkOrderStatus = ReferenceField('WorkOrderStatus', required=True, dbref=True)
    fkStoreNumber = ReferenceField('Store', required=True, dbref=True)
    meta = {'collection': 'WorkOrder'}

    def to_file(self):
        return GridFSProxy(self)

    def __str__(self):
        return f'{self.workOrderName} - {self.fkWorkOrderStatus.status}'
