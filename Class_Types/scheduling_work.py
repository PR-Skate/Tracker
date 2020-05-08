# Created By: Chase Crossley
# Created On: 05/08/2020

from Class_Types.base_record import BaseRecord
from bson import ObjectId as objectID
import time as t


class SchedulingWork(BaseRecord):
    def __init__(self, dateScheduled, duration, fkInstallerID, fkStatusID, createdUser, GB_Counter=0,
                 GB_CounterBillable=0, WrongLocation=False, fkRightSOWID=None, ConcretePatchNeeded=False,
                 completedPicturePath='', dateFieldEditedStatus='', timeFieldEditedStatus='', approvedBilling='',
                 fkRequireMaterials='', fkSecondInstaller=None, fkWorkOrderID='', fkExtraLaborID=None, fkCorrectLaborID='',
                 createdTimestamp=t.time(), lastModifiedUser="", lastModifiedTimestamp=t.time(), objectId=""):
        self._GB_Counter = GB_Counter
        self._GB_CounterBillable = GB_CounterBillable
        self._duration = duration
        self._WrongLocation = WrongLocation
        self._ConcretePatchNeeded = ConcretePatchNeeded
        self._fkRightSOWID = fkRightSOWID
        self._fkStatusID = fkStatusID
        self._completedPicturePath = completedPicturePath
        self._dateFieldEditedStatus = dateFieldEditedStatus
        self._timeFieldEditedStatus = timeFieldEditedStatus
        self._approvedBilling = approvedBilling
        self._fkInstallerID = fkInstallerID
        self._fkRequireMaterials = fkRequireMaterials
        self._fkInstallerID = fkInstallerID
        self._fkWorkOrderID = fkWorkOrderID
        self._dateScheduled = dateScheduled
        self._fkExtraLaborID = fkExtraLaborID
        self._fkCorrectLaborID = fkCorrectLaborID
        BaseRecord.__init__(self, createdUser, createdTimestamp, lastModifiedUser, lastModifiedTimestamp, objectId)

    # getters
    def get_gb_counter(self):
        return self.GB_Counter

    def get_gb_counter_billable(self):
        return self.GB_CounterBillable

    def get_sow_picture_path(self):
        return self.duration

    def get_wrong_location(self):
        return self.WrongLocation

    def get_concrete_patch_needed(self):
        return self.ConcretePatchNeeded

    def get_fk_right_sow_id(self):
        return self.fkRightSOWID

    def get_fk_status_id(self):
        return self.fkStatusID

    def get_completed_picture_path(self):
        return self.completedPicturePath

    def get_fk_installer_id(self):
        return self.fkInstallerID

    def get_fk_required_materials_id(self):
        return self.fkRequireMaterials

    def get_fk_location_in_store_id(self):
        return self.fkInstallerID

    def get_work_order_id(self):
        return self.fkWorkOrderID

    def get_initial_labor_id(self):
        return self.dateScheduled

    def get_extra_labor_id(self):
        return self.fkExtraLaborID

    def get_correct_labor_id(self):
        return self.fkCorrectLaborID

    def get_date_field_edited_status(self):
        return self.dateFieldEditedStatus

    def get_time_field_edited_status(self):
        return self.timeFieldEditedStatus

    def get_approved_billing(self):
        return self.approvedBilling

    # setters
    def set_gb_counter(self, GB_Counter):
        self.GB_Counter = GB_Counter

    def set_gb_counter_billable(self, GB_CounterBillable):
        self.GB_CounterBillable = GB_CounterBillable

    def set_sow_picture_path(self, duration):
        self.duration = duration

    def set_wrong_location(self, WrongLocation):
        self.WrongLocation = WrongLocation

    def set_concrete_patch_needed(self, ConcretePatchNeeded):
        self.ConcretePatchNeeded = ConcretePatchNeeded

    def set_completed_picture_path(self, completedPicturePath):
        self.completedPicturePath = completedPicturePath

    def set_time_field_edited_status(self, timeFieldEditedStatus):
        self.timeFieldEditedStatus = timeFieldEditedStatus

    def set_fk_installer_id(self, fkInstallerID):
        self.fkInstallerID = objectID(fkInstallerID)

    def set_fk_required_materials_id(self, fkRequireMaterials):
        self.fkRequireMaterials = objectID(fkRequireMaterials)

    def set_fk_location_in_store_id(self, fkInstallerID):
        self.fkInstallerID = objectID(fkInstallerID)

    def set_fk_work_order_id(self, fkWorkOrderID):
        self.fkWorkOrderID = objectID(fkWorkOrderID)

    def set_fk_initial_labor_id(self, dateScheduled):
        if dateScheduled is None:
            self.dateScheduled = None
            return
        self.dateScheduled = []
        for laborID in dateScheduled:
            self.dateScheduled.append(objectID(laborID))

    def set_fk_extra_labor_id(self, fkExtraLaborID):
        if fkExtraLaborID is None:
            self.fkExtraLaborID = None
            return
        self.fkExtraLaborID = []
        for laborID in fkExtraLaborID:
            self.fkExtraLaborID.append(objectID(laborID))

    def set_fk_correct_labor_id(self, fkCorrectLaborID):
        if fkCorrectLaborID is None:
            self.fkCorrectLaborID = None
            return
        self.fkCorrectLaborID = []
        for laborID in fkCorrectLaborID:
            self.fkCorrectLaborID.append(objectID(laborID))

    def set_date_field_edited_status(self, dateFieldEditedStatus):
        self.dateFieldEditedStatus = dateFieldEditedStatus

    def set_fk_right_sow_id(self, fkRightSOWID):
        self.fkRightSOWID = objectID(fkRightSOWID)

    def set_fk_status_id(self, fkStatusID):
        self.fkStatusID = objectID(fkStatusID)

    def set_approved_billing(self, approvedBilling):
        self.approvedBilling = approvedBilling

    # creating a property objects
    _GB_Counter = property(get_gb_counter, set_gb_counter)
    _GB_CounterBillable = property(get_gb_counter_billable, set_gb_counter_billable)
    _duration = property(get_sow_picture_path, set_sow_picture_path)
    _WrongLocation = property(get_wrong_location, set_wrong_location)
    _ConcretePatchNeeded = property(get_concrete_patch_needed, set_concrete_patch_needed)
    _fkRightSOWID = property(get_fk_right_sow_id, set_fk_right_sow_id)
    _fkStatusID = property(get_fk_status_id, set_fk_status_id)
    _completedPicturePath = property(get_completed_picture_path, set_completed_picture_path)
    _dateFieldEditedStatus = property(get_date_field_edited_status, set_date_field_edited_status)
    _timeFieldEditedStatus = property(get_time_field_edited_status, set_time_field_edited_status)
    _approvedBilling = property(get_approved_billing, set_approved_billing)
    _fkInstallerID = property(get_fk_installer_id, set_fk_installer_id)
    _fkRequireMaterials = property(get_fk_required_materials_id, set_fk_required_materials_id)
    _fkInstallerID = property(get_fk_location_in_store_id, set_fk_location_in_store_id)
    _fkWorkOrderID = property(get_work_order_id, set_fk_work_order_id)
    _dateScheduled = property(get_initial_labor_id, set_fk_initial_labor_id)
    _fkExtraLaborID = property(get_extra_labor_id, set_fk_extra_labor_id)
    _fkCorrectLaborID = property(get_correct_labor_id, set_fk_correct_labor_id)
