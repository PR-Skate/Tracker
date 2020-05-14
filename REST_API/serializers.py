from rest_framework import serializers
from rest_framework_mongoengine.serializers import DocumentSerializer, EmbeddedDocumentSerializer
from Class_Types import *


class BaseSerializer(DocumentSerializer):
    createdUser = serializers.CharField(required=True)


class LocationInStoreSerializer(DocumentSerializer):
    class Meta:
        model = LocationInStore
        fields = model.get_fields()
        optional_fields = model.get_optional_fields()
        depth = 1


class ScopeOfWorkSerializer(DocumentSerializer):
    class Meta:
        model = ScopeOfWork
        fields = model.get_fields()
        optional_fields = model.get_optional_fields()
        depth = 1


class ScopeOfWorkStatusSerializer(DocumentSerializer):
    class Meta:
        model = ScopeOfWorkStatus
        fields = model.get_fields()
        optional_fields = model.get_optional_fields()
        depth = 1


class AddressSerializer(EmbeddedDocumentSerializer):
    class Meta:
        model = Address
        depth = 1


class NameSerializer(EmbeddedDocumentSerializer):
    class Meta:
        model = Name
        depth = 1


class SchedulingWorkSerializer(DocumentSerializer):
    class Meta:
        model = SchedulingWork
        fields = model.get_fields()
        optional_fields = model.get_optional_fields()
        depth = 2


class OrderMaterialSerializer(DocumentSerializer):
    class Meta:
        model = OrderMaterial
        fields = model.get_fields()
        optional_fields = model.get_optional_fields()
        depth = 1


class MaterialListSerializer(DocumentSerializer):
    class Meta:
        model = MaterialList
        fields = model.get_fields()
        optional_fields = model.get_optional_fields()
        depth = 1


class MaterialItemSerializer(DocumentSerializer):
    class Meta:
        model = MaterialItem
        fields = model.get_fields()
        optional_fields = model.get_optional_fields()
        depth = 1


class WorkOrderStatusSerializer(DocumentSerializer):
    createdUser = serializers.CharField(required=True)

    class Meta:
        model = WorkOrderStatus
        fields = model.get_fields()
        optional_fields = model.get_optional_fields()
        depth = 1


class WorkOrderSerializer(DocumentSerializer):
    class Meta:
        model = WorkOrder
        fields = model.get_fields()
        optional_fields = model.get_optional_fields()
        depth = 1


class EmployeeSerializer(DocumentSerializer):
    class Meta:
        model = Employee
        fields = model.get_fields()
        optional_fields = model.get_optional_fields()
        depth = 2


class ArticleNumberSerializer(DocumentSerializer):
    class Meta:
        model = ArticleNumber
        fields = model.get_fields()
        optional_fields = model.get_optional_fields()
        depth = 1


class LaborItemSerializer(DocumentSerializer):
    class Meta:
        model = LaborItem
        fields = model.get_fields()
        optional_fields = model.get_optional_fields()
        depth = 1


class ArticleNumberStateSerializer(DocumentSerializer):
    class Meta:
        model = ArticleNumberState
        fields = model.get_fields()
        optional_fields = model.get_optional_fields()
        depth = 1


class StoreSerializer(DocumentSerializer):
    class Meta:
        model = Store
        fields = model.get_fields()
        optional_fields = model.get_optional_fields()
        depth = 2


class RegionCodeSerializer(DocumentSerializer):
    class Meta:
        model = RegionCode
        fields = model.get_fields()
        optional_fields = model.get_optional_fields()
        depth = 1


class CustomerSerializer(DocumentSerializer):
    class Meta:
        model = Customer
        fields = model.get_fields()
        optional_fields = model.get_optional_fields()
        depth = 1


class MicroRegionCodeSerializer(DocumentSerializer):
    class Meta:
        model = MicroRegionCode
        fields = model.get_fields()
        optional_fields = model.get_optional_fields()
        depth = 1


class PrepWorkSerializer(DocumentSerializer):
    class Meta:
        model = PrepWork
        fields = model.get_fields()
        optional_fields = model.get_optional_fields()
        depth = 1
