# Created By: Alex Peterson     Petersonalex99@gmail.com 
# Created On: 05/08/2020
#

import os
import time as t
from bson import ObjectId as objectID
from Tracker.Class_Type.base_record import BaseRecord

class PrepWork(BaseRecord):
    def __init__(self, prepID, downloadMLX, excelInspectUploaded, inspectionPictures, postedSync, formComplete, concretePatchNeeded, materialOrderNumberHD,
        cpn_eta, inspectionDueDates, lastDateChecked, fkCreatedUser, createdTimeStamp, fkLastModifiedUser, lastModifiedTimeStamp, fkWorkOrderName):

        self.prepID = prepID
        self.downloadMLX = downloadMLX
        self.excelInspectUploaded = excelInspectUploaded
        self.inspectionPictures = inspectionPictures
        self.postedSync = postedSync

        self.formComplete = formComplete
        self.concretePatchNeeded = concretePatchNeeded
        self.materialOrderNumberHD = materialOrderNumberHD
        self.cpn_eta = cpn_eta
        self.inspectionDueDates = inspectionDueDates

        self.lastDateChecked = lastDateChecked
        self.fkWorkOrderNames = fkWorkOrderName
        BaseRecord.__init__(self, fkCreatedUser, createdTimeStamp, fkLastModifiedUser, lastModifiedTimeStamp)


    #getters 
    def get_prep_id(self):
        return self._prepID

    def get_download_mlx(self):
        return self._downloadMLX

    def get_excel_inspect_upload(self):
        return self._excelInsepctUpload

    def get_inspection_pictures(self):
        return self._inspectionPictures

    def get_posted_sync(self):
        return self._postedSync



    def get_form_complete(self):
        return self._formComplete

    def get_concrete_patch_needed(self):
        return self._concretePatchNeeded

    def get_material_order_number_hd(self):
        return self._materialOrderNumber

    def get_cpn_eta(self):
        return self._cpn_eta

    def get_inspection_due_dates(self):
        return self._inspectionDueDates



    def get_last_date_checked(self):
        return self._lastDateChecked

    def get_fk_work_order_names(self):
        return self._fkWorkOrderNames


    #setters
    def set_prep_id(self, __prep_id ):
        self.prepID = __prep_id

    def set_download_mlx(self, __download_mlx ):
        self.downloadMLX = __download_mlx

    def set_excel_inspect_upload(self, __excel_inspect_upload ):
        self.excelInspectUpload = __excel_inspect_upload

    def set_inspection_pictures(self, __inspection_pictures ):
        self.inspectionPictures = __inspection_pictures

    def set_posted_sync(self, __posted_sync ):
        self.postedSync = __posted_sync




    def set_form_complete(self, __form_complete ):
        self.formComplete = __form_complete

    def set_concrete_patch_needed(self, __concrete_patch_needed ):
        self.concretePatchHD = __concrete_patch_needed

    def set_material_order_number_hd(self, __material_order_number_hd ):
        self.materialOrderNumberHD = __material_order_number_hd

    def set_cpn_eta(self, __cpn_eta ):
        self.cpn_eta = __cpn_eta

    def set_inspection_due_dates(self, __inspection_due_dates ):
        self.insepctionDueDates = __inspection_due_dates




    def set_last_date_checked(self, __last_date_checked):
        self.lastDateChecked = __last_date_checked
        
    def set_fk_work_order_names(self, __fk_work_order_names ):
        if not __fk_work_order_names:
               raise ValueError("Work order name must have value. Work Order Name: {wod}".format(wod= __fk_work_order_names)) 
        self.fkWorkOrderNames = objectID(__fk_work_order_names)


        #properties:
        prep_id = property( get_prep_id, set_prep_id)
        download_mlx = property( get_download_mlx, set_download_mlx)
        excel_inspect_upload = property( get_excel_inspect_upload, set_excel_inspect_upload)
        inspection_pictures = property( get_inspection_pictures, set_inspection_pictures)
        posted_sync = property( get_posted_sync, set_posted_sync)

        form_complete = property( get_form_complete, set_form_complete)
        concrete_patch_needed = property( get_concrete_patch_needed, set_concrete_patch_needed)
        material_order_number_hd = property( get_material_order_number_hd, set_material_order_number_hd)
        cpn_eta = property( get_cpn_eta, set_cpn_eta)
        inspection_due_dates = property( get_inspection_due_dates, set_inspection_due_dates)

        last_date_checked = property( get_last_date_checked, set_last_date_checked)
        fk_work_order_names = property( get_fk_work_order_names, set_fk_work_order_names)