from rest_framework import serializers
from rest_framework_mongoengine.serializers import DocumentSerializer, EmbeddedDocumentSerializer
from Class_Types import *


class BaseSerializer(DocumentSerializer):
    createdUser = serializers.CharField(required=True)


class LocationInStoreSerializer(BaseSerializer):
    class Meta:
        model = LocationInStore
        fields = model.get_fields()
        depth = 1


class ScopeOfWorkSerializer(BaseSerializer):
    class Meta:
        model = ScopeOfWork
        fields = model.get_fields()
        depth = 1


class ScopeOfWorkStatusSerializer(BaseSerializer):
    class Meta:
        model = ScopeOfWorkStatus
        fields = model.get_fields()
        depth = 1


class AddressSerializer(EmbeddedDocumentSerializer):
    class Meta:
        model = Address
        fields = '__all__'
        depth = 1


class NameSerializer(EmbeddedDocumentSerializer):
    class Meta:
        model = Name
        fields = '__all__'
        depth = 1


class SchedulingWorkSerializer(BaseSerializer):
    weekOneNameOfContact = NameSerializer(many=False)
    weekFourNameOfContact = NameSerializer(many=False)

    class Meta:
        model = SchedulingWork
        fields = model.get_fields()
        depth = 2


class OrderMaterialSerializer(BaseSerializer):
    class Meta:
        model = OrderMaterial
        fields = model.get_fields()
        depth = 1


class MaterialListSerializer(BaseSerializer):
    class Meta:
        model = MaterialList
        fields = model.get_fields()
        depth = 1


class MaterialItemSerializer(BaseSerializer):
    class Meta:
        model = MaterialItem
        fields = model.get_fields()
        depth = 1


class WorkOrderStatusSerializer(BaseSerializer):
    createdUser = serializers.CharField(required=True)

    class Meta:
        model = WorkOrderStatus
        fields = model.get_fields()
        depth = 1


class WorkOrderSerializer(BaseSerializer):
    class Meta:
        model = WorkOrder
        fields = model.get_fields()
        depth = 1


class EmployeeSerializer(BaseSerializer):
    address = AddressSerializer(many=False)

    class Meta:
        model = Employee
        fields = model.get_fields()
        depth = 2


class ArticleNumberSerializer(BaseSerializer):
    class Meta:
        model = ArticleNumber
        fields = model.get_fields()
        depth = 1


class LaborItemSerializer(BaseSerializer):
    class Meta:
        model = LaborItem
        fields = model.get_fields()
        depth = 1


class ArticleNumberStateSerializer(BaseSerializer):
    class Meta:
        model = ArticleNumberState
        fields = model.get_fields()
        depth = 1


class StoreSerializer(BaseSerializer):
    address = AddressSerializer()
    storeManagerName = NameSerializer()
    opsManagerName = NameSerializer()
    managerName = NameSerializer()
    overnightManagerName = NameSerializer()

    class Meta:
        model = Store
        fields = model.get_fields()
        depth = 2


class RegionCodeSerializer(BaseSerializer):
    class Meta:
        model = RegionCode
        fields = model.get_fields()
        depth = 1


class CustomerSerializer(BaseSerializer):
    class Meta:
        model = Customer
        fields = model.get_fields()
        depth = 1


class MicroRegionCodeSerializer(BaseSerializer):
    class Meta:
        model = MicroRegionCode
        fields = model.get_fields()
        depth = 1


class PrepWorkSerializer(BaseSerializer):
    class Meta:
        model = PrepWork
        fields = model.get_fields()
        depth = 1
