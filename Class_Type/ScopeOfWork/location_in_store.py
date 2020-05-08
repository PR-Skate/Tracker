# Created By: Chase Crossley
# Created On: 05/07/2020

from Class_Type.base_record import BaseRecord
from bson import ObjectId as objectID
import time as t


class LocationInStore(BaseRecord):
    def __init__(self, department, aisle, bay, tower, plumbingInLocation, electricalInLocation, fkStoreNumber,
                 createdUser, level=None, plumbingPicturePath='', electricalPicturePath='', fkMaterialList=None,
                 createdTimestamp=t.time(), lastModifiedUser="", lastModifiedTimestamp=t.time(), objectId=""):
        self._department = department
        self._aisle = aisle
        self._bay = bay
        self._tower = tower
        self._level = level
        self._plumbingInLocation = plumbingInLocation
        self._plumbingPicturePath = plumbingPicturePath
        self._electricalInLocation = electricalInLocation
        self._electricalPicturePath = electricalPicturePath
        self._fkMaterialList = fkMaterialList
        self._fkStoreNumber = fkStoreNumber
        BaseRecord.__init__(self, createdUser, createdTimestamp, lastModifiedUser, lastModifiedTimestamp, objectId)

    # getters
    def get_department(self):
        return self.department

    def get_aisle(self):
        return self.aisle

    def get_bay(self):
        return self.bay

    def get_tower(self):
        return self.tower

    def get_level(self):
        return self.level

    def get_plumbing_in_location(self):
        return self.plumbingInLocation

    def get_plumbing_picture_path(self):
        return self.plumbingPicturePath

    def get_electrical_in_location(self):
        return self.electricalInLocation

    def get_electrical_picture_path(self):
        return self.plumbingPicturePath

    def get_fk_material_list(self):
        return self.fkMaterialList

    def get_fk_store_number(self):
        return self.fkStoreNumber

    # setters
    def set_department(self, department):
        self.department = department

    def set_aisle(self, aisle):
        self.aisle = aisle

    def set_bay(self, bay):
        self.bay = bay

    def set_tower(self, tower):
        self.tower = tower

    def set_level(self, level):
        self.level = level

    def set_electrical_in_location(self, electricalInLocation):
        self.electricalInLocation = electricalInLocation

    def set_electrical_picture_path(self, electricalPicturePath):
        self.electricalPicturePath = electricalPicturePath

    def set_plumbing_in_location(self, plumbingInLocation):
        self.plumbingInLocation = plumbingInLocation

    def set_plumbing_picture_path(self, plumbingPicturePath):
        self.plumbingPicturePath = plumbingPicturePath

    def set_fk_material_list(self, fkMaterialList):
        if fkMaterialList is None:
            self.fkMaterialList = None
            return
        self.fkMaterialList = []
        for material in fkMaterialList:
            self.fkMaterialList.append(objectID(material))

    def set_fk_store_number(self, fkStoreNumber):
        self.fkStoreNumber = objectID(fkStoreNumber)

    # creating a property objects
    _department = property(get_department, set_department)
    _aisle = property(get_aisle, set_aisle)
    _bay = property(get_bay, set_bay)
    _tower = property(get_tower, set_tower)
    _level = property(get_level, set_level)
    _plumbingInLocation = property(get_plumbing_in_location, set_plumbing_in_location)
    _plumbingPicturePath = property(get_plumbing_picture_path, set_plumbing_picture_path)
    _electricalInLocation = property(get_electrical_in_location, set_electrical_in_location)
    _electricalPicturePath = property(get_electrical_picture_path, set_electrical_picture_path)
    _fkMaterialList = property(get_fk_material_list, set_fk_material_list)
    _fkStoreNumber = property(get_fk_store_number, set_fk_store_number)
