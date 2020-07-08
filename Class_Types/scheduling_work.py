# Created By: Chase Crossley
# Created On: 05/08/2020
import datetime

from mongoengine import IntField, DecimalField, DateTimeField, EmbeddedDocumentField, BooleanField, ReferenceField, \
    DateField, ListField, StringField

from Class_Types import Employee, WorkOrder
from Class_Types.Embeded_Documents.embeded_classes import Name
from Class_Types.base_record import BaseRecord


class SchedulingWork(BaseRecord):
    GB_Counter = IntField(default=0)  # GB = Go Back
    _truckDate = DateField(db_field='truckDate')  # MAYBE STORED SOMEWHERE ELSE/DERIVED
    _dateScheduled = DateField(required=True, db_field='dateScheduled')  # startDate
    _duration = DecimalField(db_field='duration', min_value=0.0)
    endDate = DateField()
    receivingDate = DateField()  # OPTIONAL
    weekOneCallDate = DateField()  # CALCULATED
    weekOneContact = BooleanField(default=False)  # OPTIONAL
    notCompleted = ListField(StringField())
    weekOneNameOfContact = EmbeddedDocumentField(Name)  # OPTIONAL
    weekFourCallDate = DateField()  # CALCULATED
    weekFourContact = BooleanField(default=False)
    weekFourNameOfContact = EmbeddedDocumentField(Name)  # OPTIONAL
    formComplete = BooleanField()  # OPTIONAL
    fkInstallerID = ReferenceField(Employee, dbref=True, required=True)
    fkSecondInstallerID = ReferenceField(Employee, dbref=True)  # OPTIONAL
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

    def __str__(self):
        return f'{self.fkWorkOrderID.WorkOrderName} - Form Complete:{self.formComplete}'
