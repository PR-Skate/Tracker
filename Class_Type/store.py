# Created By: Alex Peterson     Petersonalex99@gmail.com
# Created On: 05/07/2020
#

import os
import time as t
from bson import ObjectId as objectID
from bson import I
from Tracker.Class_Type.base_record import BaseRecord

class Store(BaseRecord):
    # constructor:
    def __init__(self, storeNumber, fkCustomer, address, phoneNumber,   country, region, division, awardedVendor, storeManagerName, storeManagerEmail, 
        opsManagerName, opsManagerEmail, managerName, managerEmail, overnightManagerName, overnightManagerEmail, overnightCrew, overnightAccess, noiseOrdinance, 
        timeCuttOff, fkRegionCode, fkMicroRegionCode, longitude, latitude, active, installationDueDates, fiscalWeek, fkCreatedUser ="", createdTimeStamp = t.time(),fkLastModifiedUser ="", 
        lastModifiedTimeStamp = t.time()
    ):

        self.storeNumber = storeNumber
        self.fkCustomer = fkCustomer
        self.address = address
        self.phoneNumber = phoneNumber
        self.country = country

        self.region = region
        self.division = division
        self.awardedVendor = awardedVendor
        self.storeManagerName = storeManagerName
        self.storeManagerEmail = storeManagerEmail

        self.opsManagerName = opsManagerName
        self.opsManagerEmail = opsManagerEmail
        self.managerName = managerName
        self.managerEmail = managerEmail
        self.overnightManagerName = overnightManagerName

        self.overnightManagerEmail = overnightManagerEmail
        self.overnightCrew = overnightCrew
        self.overnightAccess = overnightAccess
        self.noiseOrdinance = noiseOrdinance
        self.timeCuttOff = timeCuttOff

        self.fkRegionCode = fkRegionCode
        self.fkMicroRegionCode = fkMicroRegionCode
        self.longitude = longitude
        self.latitude = latitude
        self.active = active

        self.installationDueDates = installationDueDates
        self.fiscalWeek = fiscalWeek
        BaseRecord.__init__(self, fkCreatedUser, createdTimeStamp, fkLastModifiedUser, lastModifiedTimeStamp)

    #getters:
    def get_store_number(self):
        return self._storeNumber

    def get_fk_customer(self):
        return self._fkCustomer

    def get_address(self):
        return self._address

    def get_phoneNumber(self):
        return self._phoneNumber

    def get_country(self):
        return self._country



    def get_region(self):
        return self._region

    def get_division(self):
        return self._division

    def get_awarded_vendor(self):
        return self._awardedVendor

    def get_store_manager_name(self):
        return self._storeManagerName

    def get_store_manager_email(self):
        return self._storeManagerEmail



    def get_ops_manager_name(self):
        return self._opsManagerName

    def get_ops_manager_email(self):
        return self._opsManagerEmail

    def get_manager_name(self):
        return self._managerName

    def get_manager_email(self):
        return self._managerEmail

    def get_overnight_manager_name(self):
        return self._overnightManagerName



    def get_overnight_manager_email(self):
        return self._overnightManagerEmail

    def get_overnight_crew(self):
        return self._overnightCrew

    def get_overnight_access(self):
        return self._overnightAccess

    def get_noise_ordinance(self):
        return self._noiseOrdinance

    def get_time_cut_off(self):
        return self._timeCutOff



    def get_fk_region_code(self):
        return self._fkRegionCode

    def get_fk_micro_region_code(self):
        return self._fkMicroRegionCode

    def get_longitude(self):
        return self._longitude

    def get_latitude(self):
        return self._latitude

    def get_active(self):
        return self._active



    def get_installation_due_dates(self):
        return self._installationDueDates

    def get_fiscal_week(self):
        return self._fiscalWeek

    
    #setters:
    def set_store_number(self, __store_number ):
        self.storeNumber = __store_number

    def set_fk_customer(self, __fk_customer ):
        if not __fk_customer:
           raise ValueError("Customer must have value. Customer: {customer}".format(customer= __fk_customer)) 
        self.fkCustomer = objectID(__fk_customer)

    def set_address(self, __address ):
        self._address = __address

    def set_phone_number(self, __phone_number ):
        self.phoneNumber = __phone_number

    def set_country(self, __country ):
        self._country = __country



    def set_region(self, __region ):
        self._region = __region

    def set_division(self, __division ):
        self._division = __division

    def set_store_awarded_vendor(self, __awarded_vendor ):
        self.awardedVendor = __awarded_vendor

    def set_store_manager_name(self, __store_manager_name ):
        self.storeManagerName = __store_manager_name

    def set_store_manager_email(self, __store_manager_email ):
        self.storeManagerEmail = __store_manager_email



    def set_ops_manager_name(self, __ops_manager_name ):
        self.opsManagerName = __ops_manager_name

    def set_ops_manager_email(self, __ops_manager_email ):
        self.opsManagerEmail = __ops_manager_email

    def set_manager_name(self, __manager_name ):
        self.managerName = __manager_name

    def set_manager_email(self, __manager_email ):
        self.managerEmail = __manager_email

    def set_overnight_manager_name(self, __overnight_manager_name ):
        self.overnightManagerName = __overnight_manager_name



    def set_overnight_manager_email(self, __overnight_manager_email ):
        self.overnightManagerEmail = __overnight_manager_email

    def set_overnight_crew(self, __overnight_crew ):
        self.overnightCrew = __overnight_crew

    def set_overnight_access(self, __overnight_access ):
        self.overnightAccess = __overnight_access

    def set_noise_ordinance(self, __noise_ordinance ):
        self.noiseOrdinance = __noise_ordinance

    def set_time_cut_off(self, __time_cut_off ):
        self.timeCuttOff = __time_cut_off



    def set_fk_region_code(self, __fk_region_code ):
        if not _Store__fk_region_code:
            raise ValueError("Region code must have value. Region Code: {region_code}".format(region_code= __fk_region_code)) 
        self.fkRegionCode = objectID(__fk_region_code)

    def set_fk_micro_region_code(self, __fk_micro_region_code ):
        if not _Store__fk_micro_region_code:
            raise ValueError("Micro region code must have value. Micro region Code: {micro_region_code}".format(micro_region_code= __fk_micro_region_code))
        self.fkMicroRegionCode = objectID(__fk_micro_region_code)

    def set_longitude(self, __longitude ):
        self._longitude = __longitude

    def set_latitude(self, __latitude ):
        self._latitude = __latitude

    def set_active(self, __active ):
        self._active = __active



    def set_installation_due_dates(self, __installation_due_dates ):
        self.isntallationDueDates = __installation_due_dates

    def set_fiscal_week(self, __fiscal_week ):
        self.fiscalWeek = __fiscal_week


    #properties:
    store_number = property(get_store_number, set_store_number)
    fk_customer = property(get_fk_customer, set_fk_customer)
    address_ = property(get_address, set_address)
    phone_number = property(get_phoneNumber, set_phone_number)
    country_ = property(get_country, set_country)

    region_ = property(get_region, set_region)
    division_ = property(get_division, set_division)
    awarded_vendor = property(get_awarded_vendor, set_store_awarded_vendor)
    store_manager_name = property(get_store_manager_name, set_store_manager_name)
    store_manager_email = property(get_store_manager_email, set_store_manager_email)

    ops_manager_name = property(get_ops_manager_name, set_ops_manager_name)
    ops_manager_email = property(get_ops_manager_email, set_ops_manager_email)
    manager_name = property(get_manager_name, set_manager_name)
    manager_email = property(get_manager_email, set_manager_email)
    overnight_manager_name= property(get_overnight_manager_name, set_overnight_manager_name)

    overnight_manager_email = property(get_overnight_manager_email, set_overnight_manager_email)
    overnight_crew = property(get_overnight_crew, set_overnight_crew)
    overnight_access = property(get_overnight_access, set_overnight_access)
    noise_ordinance = property(get_noise_ordinance, set_noise_ordinance)
    time_cutt_off = property(get_time_cut_off, set_time_cut_off)

    fk_region_code= property(get_fk_region_code, set_fk_region_code)
    fk_micro_region_code= property(get_fk_micro_region_code, set_fk_micro_region_code)
    longitude_ = property(get_longitude, set_longitude)
    latitude_ = property(get_latitude, set_latitude)
    active_ = property(get_active, set_active)

    installation_due_dates = property(get_installation_due_dates, set_installation_due_dates)
    fiscal_week = property(get_fiscal_week, set_fiscal_week)


    #Still to do:
    # format cordinates