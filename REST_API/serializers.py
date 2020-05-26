from rest_framework_mongoengine.serializers import DocumentSerializer, EmbeddedDocumentSerializer
from rest_framework import serializers
from Class_Types import *


class BaseSerializer(DocumentSerializer):
    createdUser = serializers.CharField(required=True)
    lastModifiedUser = serializers.CharField(allow_null=True, allow_blank=True, required=False)

    def validate(self, attrs):
        model = self.Meta().__getattribute__("model")
        not_present_required_fields = list()
        for field in model.get_required_fields():
            if field not in attrs:
                not_present_required_fields.append(
                    "{field} is required and should contain some value.".format(field=field))

        if not_present_required_fields:
            raise serializers.ValidationError(
                '\n'.join(not_present_required_fields)
            )
        return attrs


class LocationInStoreSerializer(BaseSerializer):
    class Meta:
        model = LocationInStore
        fields = model.get_fields()


class ScopeOfWorkSerializer(BaseSerializer):
    class Meta:
        model = ScopeOfWork
        fields = model.get_fields()


class ScopeOfWorkStatusSerializer(BaseSerializer):
    class Meta:
        model = ScopeOfWorkStatus
        fields = model.get_fields()


class AddressSerializer(EmbeddedDocumentSerializer):
    class Meta:
        model = Address
        fields = model.get_fields()


class NameSerializer(EmbeddedDocumentSerializer):
    firstName = serializers.CharField(required=True)
    lastName = serializers.CharField(allow_null=True, allow_blank=True, required=False)

    class Meta:
        model = Name
        fields = ['firstName', 'lastName']


class SchedulingWorkSerializer(BaseSerializer):
    weekOneNameOfContact = NameSerializer(many=False)
    weekFourNameOfContact = NameSerializer(many=False)
    dateScheduled = serializers.DateField(required=True)
    truckDate = serializers.DateField(required=True)
    duration = serializers.DecimalField(decimal_places=2, max_digits=5, required=True)

    class Meta:
        model = SchedulingWork
        fields = model.get_fields()
        depth = 2


class OrderMaterialSerializer(BaseSerializer):
    class Meta:
        model = OrderMaterial
        fields = model.get_fields()


class MaterialListSerializer(BaseSerializer):
    class Meta:
        model = MaterialList
        fields = model.get_fields()


class MaterialItemSerializer(BaseSerializer):
    class Meta:
        model = MaterialItem
        fields = model.get_fields()


class WorkOrderStatusSerializer(BaseSerializer):
    class Meta:
        model = WorkOrderStatus
        fields = model.get_fields()


class WorkOrderSerializer(BaseSerializer):
    class Meta:
        model = WorkOrder
        fields = model.get_fields()


class EmployeeSerializer(BaseSerializer):
    name = NameSerializer(many=False)
    passwordHash = serializers.CharField(min_length=8, required=True)

    class Meta:
        model = Employee
        fields = model.get_fields()
        depth = 2


class ArticleNumberSerializer(BaseSerializer):
    class Meta:
        model = ArticleNumber
        fields = model.get_fields()


class LaborItemSerializer(BaseSerializer):
    class Meta:
        model = LaborItem
        fields = model.get_fields()


class ArticleNumberStateSerializer(BaseSerializer):
    class Meta:
        model = ArticleNumberState
        fields = model.get_fields()


class StoreSerializer(BaseSerializer):
    address = AddressSerializer(many=False)
    storeManagerName = NameSerializer(many=False)
    opsManagerName = NameSerializer(many=False)
    managerName = NameSerializer(many=False)
    overnightManagerName = NameSerializer(many=False)

    class Meta:
        model = Store
        fields = model.get_fields()
        depth = 2


class RegionCodeSerializer(BaseSerializer):
    class Meta:
        model = RegionCode
        fields = model.get_fields()


class CustomerSerializer(BaseSerializer):
    class Meta:
        model = Customer
        fields = model.get_fields()


class MicroRegionCodeSerializer(BaseSerializer):
    class Meta:
        model = MicroRegionCode
        fields = model.get_fields()


class PrepWorkSerializer(BaseSerializer):
    class Meta:
        model = PrepWork
        fields = model.get_fields()
