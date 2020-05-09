# Created By: Chase Crossley
# Created On: 05/08/2020

from Class_Types.base_record import BaseRecord
from bson import ObjectId as objectID
import time as t


class SchedulingWork(BaseRecord):
    def __init__(self, dateScheduled, duration, endDate, truckDate, weekOneCallDate, weekFourCallDate, createdUser,
                 fkInstallerID=None, GB_Counter=0, receivingDate='', weekOneContact='', weekOneNameOfContact='',
                 weekFourContact='', weekFourNameOfContact='', formComplete='', fkSecondInstallerID=None,
                 fkWorkOrderID=None, createdTimestamp=t.time(), lastModifiedUser='', lastModifiedTimestamp=t.time(),
                 objectId=''):
        self._GB_Counter = GB_Counter
        self._truckDate = truckDate
        self._duration = duration
        self._receivingDate = receivingDate
        self._weekOneContact = weekOneContact
        self._weekOneNameOfContact = weekOneNameOfContact
        self._endDate = endDate
        self._weekFourContact = weekFourContact
        self._formComplete = formComplete
        self._weekOneCallDate = weekOneCallDate
        self._weekFourCallDate = weekFourCallDate
        self._fkInstallerID = fkInstallerID
        self._fkSecondInstallerID = fkSecondInstallerID
        self._weekFourNameOfContact = weekFourNameOfContact
        self._fkInstallerID = fkInstallerID
        self._fkWorkOrderID = fkWorkOrderID
        self._dateScheduled = dateScheduled
        BaseRecord.__init__(self, createdUser, createdTimestamp, lastModifiedUser, lastModifiedTimestamp, objectId)

    # getters
    def get_gb_counter(self):
        return self.GB_Counter

    def get_truck_date(self):
        return self.truckDate

    def get_duration(self):
        return self.duration

    def get_receiving_date(self):
        return self.receivingDate

    def get_week_one_contact(self):
        return self.weekOneContact

    def get_week_one_name_of_contact(self):
        return self.weekOneNameOfContact

    def get_end_date(self):
        return self.endDate

    def get_week_four_contact(self):
        return self.weekFourContact

    def get_fk_installer_id(self):
        return self.fkInstallerID

    def get_week_four_name_of_contact(self):
        return self.weekFourNameOfContact

    def get_fk_second_installer_id(self):
        return self.fkSecondInstallerID

    def get_work_order_id(self):
        return self.fkWorkOrderID

    def get_date_scheduled(self):
        return self.dateScheduled

    def get_form_complete(self):
        return self.formComplete

    def get_week_one_call_date(self):
        return self.weekOneCallDate

    def get_week_four_call_date(self):
        return self.weekFourCallDate

    # setters
    def set_gb_counter(self, GB_Counter):
        self.GB_Counter = GB_Counter

    def set_truck_date(self, truckDate):
        self.truckDate = truckDate

    def set_duration(self, duration):
        self.duration = duration

    def set_receiving_date(self, receivingDate):
        self.receivingDate = receivingDate

    def set_week_one_contact(self, weekOneContact):
        self.weekOneContact = weekOneContact

    def set_week_four_contact(self, weekFourContact):
        self.weekFourContact = weekFourContact

    def set_week_one_call_date(self, weekOneCallDate):
        self.weekOneCallDate = weekOneCallDate

    def set_fk_installer_id(self, fkInstallerID):
        self.fkInstallerID = objectID(fkInstallerID)

    def set_week_four_name_of_contact(self, weekFourNameOfContact):
        self.weekFourNameOfContact = weekFourNameOfContact

    def set_fk_second_installer_id(self, fkSecondInstallerID):
        self.fkSecondInstallerID = objectID(fkSecondInstallerID)

    def set_fk_work_order_id(self, fkWorkOrderID):
        self.fkWorkOrderID = objectID(fkWorkOrderID)

    def set_date_scheduled(self, dateScheduled):
        self.dateScheduled = dateScheduled

    def set_form_complete(self, formComplete):
        self.formComplete = formComplete

    def set_week_one_name_of_contact(self, weekOneNameOfContact):
        self.weekOneNameOfContact = weekOneNameOfContact

    def set_end_date(self, endDate):
        self.endDate = endDate

    def set_week_four_call_date(self, weekFourCallDate):
        self.weekFourCallDate = weekFourCallDate

    # creating a property objects
    _GB_Counter = property(get_gb_counter, set_gb_counter)
    _truckDate = property(get_truck_date, set_truck_date)
    _duration = property(get_duration, set_duration)
    _receivingDate = property(get_receiving_date, set_receiving_date)
    _weekOneContact = property(get_week_one_contact, set_week_one_contact)
    _weekOneNameOfContact = property(get_week_one_name_of_contact, set_week_one_name_of_contact)
    _endDate = property(get_end_date, set_end_date)
    _weekFourContact = property(get_week_four_contact, set_week_four_contact)
    _formComplete = property(get_form_complete, set_form_complete)
    _weekOneCallDate = property(get_week_one_call_date, set_week_one_call_date)
    _weekFourCallDate = property(get_week_four_call_date, set_week_four_call_date)
    _fkInstallerID = property(get_fk_installer_id, set_fk_installer_id)
    _weekFourNameOfContact = property(get_week_four_name_of_contact, set_week_four_name_of_contact)
    _fkSecondInstallerID = property(get_fk_second_installer_id, set_fk_second_installer_id)
    _fkWorkOrderID = property(get_work_order_id, set_fk_work_order_id)
    _dateScheduled = property(get_date_scheduled, set_date_scheduled)
