# Created By: Chase Crossley
# Created On: 05/08/2020
from mongoengine import IntField, ImageField, BooleanField, DateField, DateTimeField, ReferenceField, StringField

from .location_in_store import BaseRecord, LocationInStore
from .scope_of_work_status import ScopeOfWorkStatus
from ..Labor_Items import LaborItem
from ..Material_Items import OrderMaterial
from ..Work_Order import WorkOrder
from ..employee import Employee

"""
 NOTES ON EVERTHING RELATING TO WORK ORDER:
 
 WO, PREP, SOW, SIGN-OFF
"""


class ScopeOfWork(BaseRecord):
    GB_Counter = IntField(default=0, min_value=0)
    GB_CounterBillable = IntField(default=0, min_value=0)
    SOWPicturePath = ImageField(required=True)
    wrongLocation = BooleanField(default=False)
    ConcretePatchNeeded = BooleanField(default=False)
    fkRightSOWID = ReferenceField('self', default=None, dbref=False)  # pop-up to fill out blank form
    fkStatusID = ReferenceField(ScopeOfWorkStatus, required=True, dbref=False)
    materialsOrderByInspector = StringField()  # multiline
    completedPicturePath = ImageField(default=None)
    dateFieldEditedStatus = DateField(default=None)
    timeFieldEditedStatus = DateTimeField(default=None)
    approvedBilling = BooleanField(default=False)
    fkInstallerID = ReferenceField(Employee, default=None, dbref=False)
    fkRequireMaterials = ReferenceField(OrderMaterial, default=None,
                                        dbref=False)  # should also update the material list in store location
    fkLocationInStoreID = ReferenceField(LocationInStore, default=None, dbref=False)
    fkLocationInStoreChangedID = ReferenceField(LocationInStore, default=None, dbref=False)
    fkWorkOrderID = ReferenceField(WorkOrder, required=True, dbref=False)
    fkInitialLaborID = ReferenceField(LaborItem, required=True, dbref=False)
    fkExtraLaborID = ReferenceField(LaborItem, default=None, dbref=False)
    fkCorrectLaborID = ReferenceField(LaborItem, default=None, dbref=False)
    meta = {'collection': 'ScopeOfWork'}

    def __str__(self):
        return f'{self.fkInitialLaborID.description} x {self.fkInitialLaborID.quantity} {self.fkStatusID}'
