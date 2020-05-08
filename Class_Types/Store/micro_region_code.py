import os
from Tracker.Class_Type.base_record import BaseRecord


class MicroRegionCode(BaseRecord):
    def __init__(self, microRegionCodeID, name):
        self.microRegionCodeID = microRegionCodeID
        self.name = name
        BaseRecord.__init__(self, 'CrEaTeD uSeR')

    def get_microRegionCodeID(self):
        return self._microRegionCodeID

    def get_name(self):
        return self._name

    def set_microRegionCodeID(self, micro_region_code_id):
        self.microRegionCodeID = micro_region_code_id

    def set_name(self, __name):
        self.microRegionCodeID = __name

    region_code = property(get_microRegionCodeID, set_microRegionCodeID)
    name_ = property(get_name, set_name)
