# Created By: Chase Crossley
# Created On: 05/08/2020
import datetime
from mongoengine import IntField, DecimalField, DateTimeField, EmbeddedDocumentField, BooleanField, ReferenceField, \
    DateField

from Class_Types import Employee, WorkOrder
from Class_Types.Embeded_Documents.embeded_classes import Name
from Class_Types.base_record import BaseRecord


class SchedulingWork(BaseRecord):
    GB_Counter = IntField(default=0)
    _truckDate = DateTimeField(db_field='truckDate')
    _dateScheduled = DateTimeField(required=True, db_field='dateScheduled')
    _duration = DecimalField(db_field='duration')
    endDate = DateTimeField()
    receivingDate = DateField()
    weekOneCallDate = DateField()
    weekOneContact = BooleanField(default=False)
    weekOneNameOfContact = EmbeddedDocumentField(Name)
    weekFourCallDate = DateField()
    weekFourContact = BooleanField(default=False)
    weekFourNameOfContact = EmbeddedDocumentField(Name)
    formComplete = BooleanField()
    fkInstallerID = ReferenceField(Employee, dbref=True)
    fkSecondInstallerID = ReferenceField(Employee, dbref=True)
    fkWorkOrderID = ReferenceField(WorkOrder, required=True, dbref=True)
    meta = {'collection': 'SchedulingWork'}

    @property
    def truckDate(self):
        return self._truckDate

    @truckDate.setter
    def truckDate(self, value):
        date = datetime.datetime.strftime(value, '%m/%d/%y')
        self._truckDate = date
        self.weekFourCallDate = date - datetime.timedelta(weeks=4)
        self.weekOneCallDate = date - datetime.timedelta(weeks=1)

    @property
    def dateScheduled(self):
        return self._dateScheduled

    @dateScheduled.setter
    def dateScheduled(self, value):
        date = datetime.datetime.strftime(value, '%m/%d/%y')
        self._dateScheduled = date
        if self._duration:
            self.endDate = date + datetime.timedelta(days=self._duration)

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        self._duration = value
        if self._dateScheduled:
            self.endDate = self._dateScheduled + datetime.timedelta(days=self._duration)
