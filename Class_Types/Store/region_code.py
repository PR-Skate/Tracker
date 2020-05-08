# Created By: Alex Peterson
# Created On: 05/07/2020
#

import os
from Tracker.Class_Type.base_record import BaseRecord


class RegionCode(BaseRecord):
    def __init__(self, regionCodeID, name):
        self.regionCodeID = regionCodeID
        self.name = name
        BaseRecord.__init__(self, 'CrEaTeD uSeR')

    def get_regionCodeID(self):
        return self._regionCodeID

    def get_name(self):
        return self._name

    def set_regionCodeID(self, region_code_id):
        self.regionCodeID = region_code_id

    def set_name(self, __name):
        self.regionCodeID = __name

    region_code = property(get_regionCodeID, set_regionCodeID)
    name_ = property(get_name, set_name)
