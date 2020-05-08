# Created By: Alex Peterson     Petersonalex99@gmail.com
# Created On: 05/07/2020
#

import os
import time as t
from bson import ObjectId as objectID
from Tracker.Class_Type.base_record import BaseRecord

class WorkOrderStatus(BaseRecord):
    # constructor:
    def __init__(self, workOrderStatusID, name, createdUser, createdTimestamp=t.time(), lastModifiedUser="", lastModifiedTimestamp=t.time(), objectId=""):
        self._workOrderStatusID = workOrderStatusID
        self._name = name
        BaseRecord.__init__(self, createdUser, createdTimestamp, lastModifiedUser, lastModifiedTimestamp)

    
    #getters:
    def get_work_order_status_id(self):
        return self._workOrderStatusID

    def get_name(self):
        return self._name


    #setters:
    def set_work_order_status_id (self, workOrderStatusID ):
        self.workOrderStatusID = workOrderStatusID
    def set_name (self, name):
        self.name = name

    _workOrderStatusID = property(get_work_order_status_id, set_work_order_status_id)
    _name = property(get_name, set_name)