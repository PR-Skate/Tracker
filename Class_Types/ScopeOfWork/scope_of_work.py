# Created By: Chase Crossley
# Created On: 05/08/2020
from mongoengine import IntField, ImageField, BooleanField, DateField, DateTimeField, ReferenceField

from .location_in_store import BaseRecord, LocationInStore
from .scope_of_work_status import ScopeOfWorkStatus
from ..Labor_Items import LaborItem
from ..Material_Items import OrderMaterial
from ..Work_Order import WorkOrder
from ..employee import Employee


class ScopeOfWork(BaseRecord):
    GB_Counter = IntField(default=0, min_value=0)
    GB_CounterBillable = IntField(default=0, min_value=0)
    SOWPicturePath = ImageField(required=True)
    WrongLocation = BooleanField(default=False)
    ConcretePatchNeeded = BooleanField(default=False)
    fkRightSOWID = ReferenceField('self', default=None, dbref=True)
    fkStatusID = ReferenceField(ScopeOfWorkStatus, required=True, dbref=True)
    completedPicturePath = ImageField(default=None)
    dateFieldEditedStatus = DateField(default=None)
    timeFieldEditedStatus = DateTimeField(default=None)
    approvedBilling = BooleanField(default=False)
    fkInstallerID = ReferenceField(Employee, default=None, dbref=True)
    fkRequireMaterials = ReferenceField(OrderMaterial, default=None, dbref=True)
    fkLocationInStoreID = ReferenceField(LocationInStore, default=None, dbref=True)
    fkWorkOrderID = ReferenceField(WorkOrder, required=True, dbref=True)
    fkInitialLaborID = ReferenceField(LaborItem, required=True, dbref=True)
    fkExtraLaborID = ReferenceField(LaborItem, default=None, dbref=True)
    fkCorrectLaborID = ReferenceField(LaborItem, default=None, dbref=True)
    meta = {'collection': 'ScopeOfWork'}

    def __str__(self):
        return f'{self.fkInitialLaborID.description} x {self.fkInitialLaborID.quantity} {self.fkStatusID}'
