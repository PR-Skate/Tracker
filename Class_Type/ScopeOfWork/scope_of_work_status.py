# Created By: Chase Crossley
# Created On: 05/07/2020

from Class_Type.base_record import BaseRecord
import time as t


class ScopeOfWorkStatus(BaseRecord):
    def __init__(self, status, createdUser, createdTimestamp=t.time(), lastModifiedUser="",
                 lastModifiedTimestamp=t.time(), objectId=""):
        self._status = status
        BaseRecord.__init__(self, createdUser, createdTimestamp, lastModifiedUser, lastModifiedTimestamp, objectId)

    # getters
    def get_status(self):
        return self.status

    # setters
    def set_status(self, status):
        self.status = status

    # creating a property objects
    _status = property(get_status, set_status)
