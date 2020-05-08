# Created By: Alex Peterson     Petersonalex99@gmail.com
# Created On: 05/07/2020
#

import os
import time as t
from bson import ObjectId as objectID
from Tracker.Class_Type.base_record import BaseRecord

class WorkOrder(BaseRecord):
    # constructor:
    def __init__(self, workOrderName, dateReceived, detail, requestingContact, statusCode, dateCompleted, inspectForStorePath, detailedReceiptPath, signageMapPath,
                partsArrivalDate, targetStartDate, fkWorkOrderStatus, fkStoreNumber, fkCreatedUser ="", createdTimeStamp = t.time(),fkLastModifiedUser ="", lastModifiedTimeStamp = t.time()):
        self._workOrderName = workOrderName
        self._dateReceived = dateReceived
        self._detail = detail
        self._requestingContact = requestingContact
        self._statusCode = statusCode

        self._dateCompleted = dateCompleted
        self._inspectForStorePath = inspectForStorePath
        self._detailedReceiptPath = detailedReceiptPath
        self._signageMapPath = signageMapPath
        self._partsArrivalDate = partsArrivalDate

        self._targetStartDate = targetStartDate
        self._fkWorkOrderStatus = fkWorkOrderStatus
        self._fkStoreNumber = fkStoreNumber
        BaseRecord.__init__(self, fkCreatedUser, createdTimeStamp, fkLastModifiedUser, lastModifiedTimeStamp)

    #getters:
    def get_work_order_name(self):
        print('test')
        return self.workOrderName

    def get_date_received(self):
        return self.dateReceived

    def get_detail(self):
        return self.detail

    def get_requesting_contact(self):
        return self.requestingContact

    def get_status_code(self):
        return self.statusCode



    def get_date_completed(self):
        return self.dateCompleted

    def get_inspect_for_store_path(self):
        return self.inspectForStorePath

    def get_detailed_receipt_path(self):
        return self.detailedReceiptPath

    def get_signage_map_path(self):
        return self.signageMapPath

    def get_parts_arrival_date(self):
        return self.partsArrivalDate



    def get_target_start_date(self):
        return self.targetStartDate

    def get_fk_work_order_status(self):
        return self.fkWorkOrderStatus

    def get_fk_store_number(self):
        return self.fkStoreNumber



    #setters:
    def set_work_order_name(self, workOrderName ):
        self.workOrderName = workOrderName

    def set_date_received(self, dateReceived ):
        self.dateReceived = dateReceived

    def set_detail(self, detail ):
        self.detail = detail

    def set_requesting_contact(self, requestingContact ):
        self.requestingContact = requestingContact

    def set_status_code(self, statusCode ):
        self.statusCode = statusCode



    def set_date_completed(self, dateCompleted):
        self.dateCompleted = dateCompleted

    def set_inspect_for_store_path(self, inspectForStorePath ):
        self.inspectForStorePath = inspectForStorePath

    def set_detailed_receipt_path(self, detailedReceiptPath ):
        self.detailedReceiptPath = detailedReceiptPath

    def set_signage_map_path(self, signageMapPath ):
        self.signageMapPath = signageMapPath

    def set_parts_arrival_date(self, partsArrivalDate ):
        self.partsArrivalDate = partsArrivalDate



    def set_target_start_date(self, targetStartDate ):
        self.targetStartDate = targetStartDate

    def set_fk_work_order_status(self, fkWorkOrderStatus ):
        if not fkWorkOrderStatus:
            raise ValueError("Work order status must have value. Work Order Status: {wos}".format(wos= fkWorkOrderStatus))
        self.fkWorkOrderStatus = objectID(fkWorkOrderStatus)

    def set_fk_store_number(self, fkStoreNumber ):
        if not fkStoreNumber:
            raise ValueError("Store number must have value. Store Number: {store_num}".format(store_num= fkStoreNumber))
        self.fkStoreNumber = objectID(fkStoreNumber)
        


    _workOrderName = property(get_work_order_name, set_work_order_name)
    _dateReceived = property(get_date_received, set_date_received)
    _detail = property(get_detail, set_detail)
    _requestingContact = property(get_requesting_contact, set_requesting_contact)
    _statusCode = property(get_status_code, set_status_code)

    _dateCompleted = property(get_date_completed, set_date_completed)
    _inspectForStorePath = property(get_inspect_for_store_path, set_inspect_for_store_path)
    _detailedReceiptPath = property(get_detailed_receipt_path, set_detailed_receipt_path)
    _signageMapPath = property(get_signage_map_path, set_signage_map_path)
    _partsArrivalDate = property(get_parts_arrival_date, set_parts_arrival_date)

    _targetStartDate = property(get_target_start_date, set_target_start_date)
    _fkWorkOrderStatus = property(get_fk_work_order_status, set_fk_work_order_status)
    _fkStoreNumber = property(get_fk_store_number, set_fk_store_number)