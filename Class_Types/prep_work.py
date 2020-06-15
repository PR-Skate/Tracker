# Created By: Alex Peterson     Petersonalex99@gmail.com 
# Created On: 05/08/2020
#
from datetime import datetime

from mongoengine import DateTimeField, BooleanField, StringField, ReferenceField

from Class_Types import BaseRecord, WorkOrder


class PrepWork(BaseRecord):
    downloadMLX = BooleanField(default=False)
    excelInspectUploaded = BooleanField(default=False)
    inspectionPictures = BooleanField(default=False)
    preWalk = BooleanField(default=False)
    postedSync = BooleanField(default=False)
    formComplete = BooleanField(default=False)
    concretePatchNeeded = BooleanField(default=False)
    materialOrderNumberHD = StringField(default='')
    cpn_eta = DateTimeField()
    inspectionDueDates = DateTimeField()
    lastDateChecked = DateTimeField(default=datetime.utcnow)
    fkWorkOrderName = ReferenceField(WorkOrder, required=True, dbref=True)
    meta = {'collection': 'PrepWork'}

    def __str__(self):
        return f'{self.fkWorkOrderName.WorkOrderName} - Form Complete:{self.formComplete}'
