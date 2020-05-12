# Created By: Chase Crossley
# Created On: 05/08/2020
from mongoengine import IntField, ImageField, BooleanField, ReferenceField, DateField, DateTimeField

from Class_Types.base_record import BaseRecord


class ScopeOfWork(BaseRecord):
    GB_Counter = IntField(default=0, min_value=0)
    GB_CounterBillable = IntField(default=0, min_value=0)
    SOWPicturePath = ImageField(required=True)
    WrongLocation = BooleanField(default=False)
    ConcretePatchNeeded = BooleanField(default=False)
    fkRightSOWID = ReferenceField('ScopeOfWork', default=None)
    fkStatusID = ReferenceField('ScopeOfWorkStatus', required=True)
    completedPicturePath = ImageField(default=None)
    dateFieldEditedStatus = DateField(default=None)
    timeFieldEditedStatus = DateTimeField(default=None)
    approvedBilling = BooleanField(default=False)
    fkInstallerID = ReferenceField('Employee', default=None)
    fkRequireMaterials = ReferenceField('OrderMaterial', default=None)
    fkLocationInStoreID = ReferenceField('LocationInStore', default=None)
    fkWorkOrderID = ReferenceField('WorkOrder', required=True)
    fkInitialLaborID = ReferenceField('LaborItem', required=True)
    fkExtraLaborID = ReferenceField('LaborItem', default=None)
    fkCorrectLaborID = ReferenceField('LaborItem', default=None)
    meta = {'collection': 'ScopeOfWork'}

