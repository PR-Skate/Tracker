# Created By: Chase Crossley
# Created On: 05/07/2020

from Class_Type.base_record import BaseRecord
from bson import ObjectId as objectID
import time as t


class LocationInStore(BaseRecord):
    def __init__(self, department, aisle, bay, tower, plumbingInLocation, electricalInLocation, fkStoreNumber,
                createdUser, level=0, plumbingPicturePath='', electricalPicturePath='', fkMaterialList=None,
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
        if not department:
            raise ValueError("department must have value. department: {0}".format(department))
        self.department = department

    def set_aisle(self, aisle):
        if aisle < 0:
            raise ValueError("aisle must be bigger than 0, aisle: {0}".format(aisle))
        self.aisle = aisle

    def set_bay(self, bay):
        if not bay:
            raise ValueError("bay must be bigger than 0, bay: {0}".format(bay))
        self.bay = bay

    def set_tower(self, tower):
        if tower < 0:
            raise ValueError("tower must be bigger than 0, tower: {0}".format(tower))
        self.tower = tower

    def set_level(self, level):
        if level < 0:
            raise ValueError("level must be bigger than 0, level: {0}".format(level))
        self.level = level

    def set_electrical_in_location(self, electricalInLocation):
        if isinstance(electricalInLocation, bool):
            self.electricalInLocation = electricalInLocation
        else:
            self.electricalInLocation = False

    def set_electrical_picture_path(self, electricalPicturePath):
        if self._electricalInLocation and not electricalPicturePath:
            raise ValueError("electricalPicturePath must be bigger than 0, electricalPicturePath: {0}".format(electricalPicturePath))
        elif self._electricalInLocation:
            self.electricalPicturePath = electricalPicturePath

    def set_plumbing_in_location(self, plumbingInLocation):
        if isinstance(plumbingInLocation, bool):
            self.plumbingInLocation = plumbingInLocation
        else:
            self.plumbingInLocation = False

    def set_plumbing_picture_path(self, plumbingPicturePath):
        if self._plumbingInLocation and not plumbingPicturePath:
            raise ValueError("plumbingPicturePath must be bigger than 0, plumbingPicturePath: {0}".format(plumbingPicturePath))
        elif self._plumbingInLocation:
            self.electricalPicturePath = plumbingPicturePath

    def set_fk_material_list(self, fkMaterialList):
        self.fkMaterialList = []
        if not fkMaterialList:
            return
        for material in fkMaterialList:
            self.fkMaterialList.append(objectID(material))

    def set_fk_store_number(self, fkStoreNumber):
        if not fkStoreNumber:
            raise ValueError("FK Article Number must have value, FK Article Number: {0}".format(fkStoreNumber))
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
