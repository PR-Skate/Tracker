# Created By: Chase Crossley
# Created On: 05/08/2020
from mongoengine import IntField, ImageField, BooleanField, ReferenceField, DateField, DateTimeField
from .location_in_store import BaseRecord, LocationInStore
from .scope_of_work_status import ScopeOfWorkStatus
from ..employee import Employee
from ..Work_Order import WorkOrder
from ..Material_Items import OrderMaterial
from ..Labor_Items import LaborItem

class ScopeOfWork(BaseRecord):
    GB_Counter = IntField(default=0, min_value=0)
    GB_CounterBillable = IntField(default=0, min_value=0)
    SOWPicturePath = ImageField(required=True)
    WrongLocation = BooleanField(default=False)
    ConcretePatchNeeded = BooleanField(default=False)
    fkRightSOWID = ReferenceField('self', default=None)
    fkStatusID = ReferenceField(ScopeOfWorkStatus, required=True)
    completedPicturePath = ImageField(default=None)
    dateFieldEditedStatus = DateField(default=None)
    timeFieldEditedStatus = DateTimeField(default=None)
    approvedBilling = BooleanField(default=False)
    fkInstallerID = ReferenceField(Employee, default=None)
    fkRequireMaterials = ReferenceField(OrderMaterial, default=None)
    fkLocationInStoreID = ReferenceField(LocationInStore, default=None)
    fkWorkOrderID = ReferenceField(WorkOrder, required=True)
    fkInitialLaborID = ReferenceField(LaborItem, required=True)
    fkExtraLaborID = ReferenceField(LaborItem, default=None)
    fkCorrectLaborID = ReferenceField(LaborItem, default=None)
    meta = {'collection': 'ScopeOfWork'}
