from django.db import models
from Class_Types import *


# Create your models here.


class ModelLocationInStore(LocationInStore):
    pass


class ModelScopeOfWork(ScopeOfWork):
    pass


class ModelScopeOfWorkStatus(ScopeOfWorkStatus):
    pass


class ModelAddress(Address):
    pass


class ModelName(Name):
    pass


class ModelSchedulingWork(SchedulingWork):
    pass


class ModelOrderMaterial(OrderMaterial):
    pass


class ModelMaterialList(MaterialList):
    pass


class ModelMaterialItem(MaterialItem):
    pass


class ModelWorkOrderStatus(WorkOrderStatus):
    pass


class ModelWorkOrder(WorkOrder):
    pass


class ModelEmployee(Employee):
    pass


class ModelArticleNumber(ArticleNumber):
    pass


class ModelLaborItem(LaborItem):
    pass


class ModelArticleNumberState(ArticleNumberState):
    pass


class ModelStore(Store):
    pass


class ModelRegionCode(RegionCode):
    pass


class ModelCustomer(Customer):
    pass


class ModelMicroRegionCode(MicroRegionCode):
    pass


class ModelPrepWork(PrepWork):
    pass
