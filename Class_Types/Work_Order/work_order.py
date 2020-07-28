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
    detail = StringField(defualt='')  # multiline
    requestingContact = StringField(required=True)
    priority = StringField(required=True)
    statusCode = StringField(max_length=30, required=True)  # choices: Pending Materials, Ready Now, Other
    requestCode = StringField(max_length=30, required=True)  # choices: P-4, P-48, Other

    dateCompleted = DateField(required=True)
    inspectForStoreFile = FileField()
    detailedReceiptFile = FileField()
    signageMapFile = FileField()
    partsArrivalDate = DateField()

    targetStartDate = DateField(required=True)
    fkWorkOrderStatus = ReferenceField('WorkOrderStatus', required=True, dbref=False)
    fkStoreNumber = ReferenceField('Store', required=True, dbref=False)
    meta = {'collection': 'WorkOrder'}

    def to_file(self):
        return GridFSProxy(self)

    def __str__(self):
        return f'{self.workOrderName} - {self.fkWorkOrderStatus.status}'
