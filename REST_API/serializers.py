from rest_framework_mongoengine.serializers import DocumentSerializer, EmbeddedDocumentSerializer
from .models import *


class LocationInStoreSerializer(DocumentSerializer):
    class Meta:
        model = ModelLocationInStore
        depth = 1


class ScopeOfWorkSerializer(DocumentSerializer):
    class Meta:
        model = ModelScopeOfWork
        depth = 1


class ScopeOfWorkStatusSerializer(DocumentSerializer):
    class Meta:
        model = ModelScopeOfWorkStatus
        depth = 1


class AddressSerializer(EmbeddedDocumentSerializer):
    class Meta:
        model = ModelAddress
        depth = 1


class NameSerializer(EmbeddedDocumentSerializer):
    class Meta:
        model = ModelName
        depth = 1


class SchedulingWorkSerializer(DocumentSerializer):
    weekOneNameOfContact = NameSerializer(many=False)
    weekFourNameOfContact = NameSerializer(many=False)

    class Meta:
        model = ModelSchedulingWork
        depth = 2


class OrderMaterialSerializer(DocumentSerializer):
    class Meta:
        model = ModelOrderMaterial
        depth = 1


class MaterialListSerializer(DocumentSerializer):
    class Meta:
        model = ModelMaterialList
        depth = 1


class MaterialItemSerializer(DocumentSerializer):
    class Meta:
        model = ModelMaterialItem
        depth = 1


class WorkOrderStatusSerializer(DocumentSerializer):
    class Meta:
        model = ModelWorkOrderStatus
        depth = 1


class WorkOrderSerializer(DocumentSerializer):
    class Meta:
        model = ModelWorkOrder
        depth = 1


class EmployeeSerializer(DocumentSerializer):
    address = AddressSerializer(many=False)

    class Meta:
        model = ModelEmployee
        depth = 2


class ArticleNumberSerializer(DocumentSerializer):
    class Meta:
        model = ModelArticleNumber
        depth = 1


class LaborItemSerializer(DocumentSerializer):
    class Meta:
        model = ModelLaborItem
        depth = 1


class ArticleNumberStateSerializer(DocumentSerializer):
    class Meta:
        model = ModelArticleNumberState
        depth = 1


class StoreSerializer(DocumentSerializer):
    address = AddressSerializer()
    storeManagerName = NameSerializer()
    opsManagerName = NameSerializer()
    managerName = NameSerializer()
    overnightManagerName = NameSerializer()
    class Meta:
        model = ModelStore
        depth = 2


class RegionCodeSerializer(DocumentSerializer):
    class Meta:
        model = ModelRegionCode
        depth = 1


class CustomerSerializer(DocumentSerializer):
    class Meta:
        model = ModelCustomer
        depth = 1


class MicroRegionCodeSerializer(DocumentSerializer):
    class Meta:
        model = ModelMicroRegionCode
        depth = 1


class PrepWorkSerializer(DocumentSerializer):
    class Meta:
        model = ModelPrepWork
        depth = 1
