from rest_framework import serializers
from rest_framework_mongoengine.serializers import DocumentSerializer, EmbeddedDocumentSerializer

from Class_Types import *


class BaseSerializer(DocumentSerializer):
    createdUser = serializers.CharField(required=True)

    def validate(self, attrs):
        model = self.Meta().__getattribute__("model")
        for field in model.get_required_fields():
            if not attrs[field]:
                raise serializers.ValidationError(
                    "{field} is required and should contain some value.".format(field=field))
        return attrs


class LocationInStoreSerializer(BaseSerializer):
    class Meta:
        model = LocationInStore
        fields = model.get_fields()
        extra_kwargs = {'createdTimestamp': {'required': False, 'allow_null': True},
                        'lastModifiedUser': {'required': False, 'allow_null': True, 'allow_blank': True},
                        'lastModifiedTimestamp': {'required': False, 'allow_null': True},
                        'level': {'required': False, 'allow_null': True, 'allow_blank': True},
                        'plumbingInLocation': {'required': False, 'allow_null': True},
                        'plumbingPicturePath': {'required': False, 'allow_null': True},
                        'electricalInLocation': {'required': False, 'allow_null': True},
                        'electricalPicturePath': {'required': False, 'allow_null': True},
                        'fkMaterialList': {'required': False, 'allow_null': True}}
        depth = 1


class ScopeOfWorkSerializer(BaseSerializer):
    class Meta:
        model = ScopeOfWork
        fields = model.get_fields()
        extra_kwargs = {'createdTimestamp': {'required': False, 'allow_null': True},
                        'lastModifiedUser': {'required': False, 'allow_null': True, 'allow_blank': True},
                        'lastModifiedTimestamp': {'required': False, 'allow_null': True},
                        'GB_Counter': {'required': False, 'allow_null': True},
                        'GB_CounterBillable': {'required': False, 'allow_null': True},
                        'WrongLocation': {'required': False, 'allow_null': True},
                        'ConcretePatchNeeded': {'required': False, 'allow_null': True},
                        'fkRightSOWID': {'required': False, 'allow_null': True},
                        'completedPicturePath': {'required': False, 'allow_null': True},
                        'dateFieldEditedStatus': {'required': False, 'allow_null': True},
                        'timeFieldEditedStatus': {'required': False, 'allow_null': True},
                        'approvedBilling': {'required': False, 'allow_null': True},
                        'fkInstallerID': {'required': False, 'allow_null': True},
                        'fkRequireMaterials': {'required': False, 'allow_null': True},
                        'fkLocationInStoreID': {'required': False, 'allow_null': True},
                        'fkExtraLaborID': {'required': False, 'allow_null': True},
                        'fkCorrectLaborID': {'required': False, 'allow_null': True}}
        depth = 1


class ScopeOfWorkStatusSerializer(BaseSerializer):
    class Meta:
        model = ScopeOfWorkStatus
        fields = model.get_fields()
        extra_kwargs = {'createdTimestamp': {'required': False, 'allow_null': True},
                        'lastModifiedUser': {'required': False, 'allow_null': True, 'allow_blank': True},
                        'lastModifiedTimestamp': {'required': False, 'allow_null': True}}
        depth = 1


class AddressSerializer(EmbeddedDocumentSerializer):
    class Meta:
        model = Address
        depth = 1


class NameSerializer(EmbeddedDocumentSerializer):
    class Meta:
        model = Name
        depth = 1


class SchedulingWorkSerializer(BaseSerializer):
    weekOneNameOfContact = NameSerializer(many=False)
    weekFourNameOfContact = NameSerializer(many=False)

    class Meta:
        model = SchedulingWork
        fields = model.get_fields()
        extra_kwargs = {'createdTimestamp': {'required': False, 'allow_null': True},
                        'lastModifiedUser': {'required': False, 'allow_null': True, 'allow_blank': True},
                        'lastModifiedTimestamp': {'required': False, 'allow_null': True},
                        'GB_Counter': {'required': False, 'allow_null': True},
                        '_truckDate': {'required': False, 'allow_null': True},
                        '_duration': {'required': False, 'allow_null': True},
                        'endDate': {'required': False, 'allow_null': True},
                        'receivingDate': {'required': False, 'allow_null': True},
                        'weekOneCallDate': {'required': False, 'allow_null': True},
                        'weekOneContact': {'required': False, 'allow_null': True},
                        'weekOneNameOfContact': {'required': False, 'allow_null': True},
                        'weekFourCallDate': {'required': False, 'allow_null': True},
                        'weekFourContact': {'required': False, 'allow_null': True},
                        'weekFourNameOfContact': {'required': False, 'allow_null': True},
                        'formComplete': {'required': False, 'allow_null': True},
                        'fkInstallerID': {'required': False, 'allow_null': True},
                        'fkSecondInstallerID': {'required': False, 'allow_null': True}}
        depth = 2


class OrderMaterialSerializer(BaseSerializer):
    class Meta:
        model = OrderMaterial
        fields = model.get_fields()
        extra_kwargs = {'createdTimestamp': {'required': False, 'allow_null': True},
                        'lastModifiedUser': {'required': False, 'allow_null': True, 'allow_blank': True},
                        'lastModifiedTimestamp': {'required': False, 'allow_null': True},
                        'fkMaterialItem': {'required': False, 'allow_null': True}}
        depth = 1


class MaterialListSerializer(BaseSerializer):
    class Meta:
        model = MaterialList
        fields = model.get_fields()
        extra_kwargs = {'createdTimestamp': {'required': False, 'allow_null': True},
                        'lastModifiedUser': {'required': False, 'allow_null': True, 'allow_blank': True},
                        'lastModifiedTimestamp': {'required': False, 'allow_null': True},
                        'fkMaterialItem': {'required': False, 'allow_null': True}}
        depth = 1


class MaterialItemSerializer(BaseSerializer):
    class Meta:
        model = MaterialItem
        fields = model.get_fields()
        extra_kwargs = {'createdTimestamp': {'required': False, 'allow_null': True},
                        'lastModifiedUser': {'required': False, 'allow_null': True, 'allow_blank': True},
                        'lastModifiedTimestamp': {'required': False, 'allow_null': True}}
        depth = 1


class WorkOrderStatusSerializer(BaseSerializer):
    class Meta:
        model = WorkOrderStatus
        fields = model.get_fields()
        extra_kwargs = {'createdTimestamp': {'required': False, 'allow_null': True},
                        'lastModifiedUser': {'required': False, 'allow_null': True, 'allow_blank': True},
                        'lastModifiedTimestamp': {'required': False, 'allow_null': True}}
        depth = 1


class WorkOrderSerializer(BaseSerializer):

    class Meta:
        model = WorkOrder
        fields = model.get_fields()
        extra_kwargs = {'createdTimestamp': {'required': False, 'allow_null': True},
                        'lastModifiedUser': {'required': False, 'allow_null': True, 'allow_blank': True},
                        'lastModifiedTimestamp': {'required': False, 'allow_null': True},
                        'inspectForStorePath': {'required': False, 'allow_null': True},
                        'detailedReceiptPath': {'required': False, 'allow_null': True},
                        'signageMapPath': {'required': False, 'allow_null': True},
                        'partsArrivalDate': {'required': False, 'allow_null': True}}
        depth = 1


class EmployeeSerializer(BaseSerializer):
    passwordHash = serializers.CharField(required=True)
    class Meta:
        model = Employee
        fields = model.get_fields()
        extra_kwargs = {'createdTimestamp': {'required': False, 'allow_null': True},
                        'lastModifiedUser': {'required': False, 'allow_null': True, 'allow_blank': True},
                        'lastModifiedTimestamp': {'required': False, 'allow_null': True},
                        'rateOfPay': {'required': False, 'allow_null': True}}
        depth = 2


class ArticleNumberSerializer(BaseSerializer):
    class Meta:
        model = ArticleNumber
        fields = model.get_fields()
        extra_kwargs = {'createdTimestamp': {'required': False, 'allow_null': True},
                        'lastModifiedUser': {'required': False, 'allow_null': True, 'allow_blank': True},
                        'lastModifiedTimestamp': {'required': False, 'allow_null': True},
                        'UsedByInspectionCompanyButNotPrSkate': {'required': False, 'allow_null': True},
                        'Capital': {'required': False, 'allow_null': True}}
        depth = 1


class LaborItemSerializer(BaseSerializer):
    class Meta:
        model = LaborItem
        fields = model.get_fields()
        extra_kwargs = {'createdTimestamp': {'required': False, 'allow_null': True},
                        'lastModifiedUser': {'required': False, 'allow_null': True, 'allow_blank': True},
                        'lastModifiedTimestamp': {'required': False, 'allow_null': True},
                        'quantity': {'required': False, 'allow_null': True},
                        'fkArticleNumberState': {'required': False, 'allow_null': True}}
        depth = 1


class ArticleNumberStateSerializer(BaseSerializer):
    class Meta:
        model = ArticleNumberState
        fields = model.get_fields()
        extra_kwargs = {'createdTimestamp': {'required': False, 'allow_null': True},
                        'lastModifiedUser': {'required': False, 'allow_null': True, 'allow_blank': True},
                        'lastModifiedTimestamp': {'required': False, 'allow_null': True}}
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
        extra_kwargs = {'createdTimestamp': {'required': False, 'allow_null': True},
                        'lastModifiedUser': {'required': False, 'allow_null': True, 'allow_blank': True},
                        'lastModifiedTimestamp': {'required': False, 'allow_null': True},
                        'storeManagerName': {'required': False, 'allow_null': True},
                        'storeManagerEmail': {'required': False, 'allow_null': True, 'allow_blank': True},
                        'opsManagerName': {'required': False, 'allow_null': True},
                        'opsManagerEmail': {'required': False, 'allow_null': True, 'allow_blank': True},
                        'managerName': {'required': False, 'allow_null': True},
                        'managerEmail': {'required': False, 'allow_null': True, 'allow_blank': True},
                        'overnightManagerName': {'required': False, 'allow_null': True},
                        'overnightManagerEmail': {'required': False, 'allow_null': True, 'allow_blank': True},
                        'overnightCrew': {'required': False, 'allow_null': True, 'allow_blank': True},
                        'overnightAccess': {'required': False, 'allow_null': True},
                        'noiseOrdinance': {'required': False, 'allow_null': True},
                        'timeCutOff': {'required': False, 'allow_null': True},
                        'fkRegionCode': {'required': False, 'allow_null': True},
                        'fkMicroRegionCode': {'required': False, 'allow_null': True},
                        'coordinates': {'required': False, 'allow_null': True},
                        'active': {'required': False, 'allow_null': True},
                        'installationDueDates': {'required': False, 'allow_null': True},
                        'inspectionDueDates': {'required': False, 'allow_null': True},
                        'fiscalWeek': {'required': False, 'allow_null': True}}
        depth = 2


class RegionCodeSerializer(BaseSerializer):
    class Meta:
        model = RegionCode
        fields = model.get_fields()
        extra_kwargs = {'createdTimestamp': {'required': False, 'allow_null': True},
                        'lastModifiedUser': {'required': False, 'allow_null': True, 'allow_blank': True},
                        'lastModifiedTimestamp': {'required': False, 'allow_null': True}}
        depth = 1


class CustomerSerializer(BaseSerializer):
    class Meta:
        model = Customer
        fields = model.get_fields()
        extra_kwargs = {'createdTimestamp': {'required': False, 'allow_null': True},
                        'lastModifiedUser': {'required': False, 'allow_null': True, 'allow_blank': True},
                        'lastModifiedTimestamp': {'required': False, 'allow_null': True}}
        depth = 1


class MicroRegionCodeSerializer(BaseSerializer):
    class Meta:
        model = MicroRegionCode
        fields = model.get_fields()
        extra_kwargs = {'createdTimestamp': {'required': False, 'allow_null': True},
                        'lastModifiedUser': {'required': False, 'allow_null': True, 'allow_blank': True},
                        'lastModifiedTimestamp': {'required': False, 'allow_null': True}}
        depth = 1


class PrepWorkSerializer(BaseSerializer):
    class Meta:
        model = PrepWork
        fields = model.get_fields()
        extra_kwargs = {'createdTimestamp': {'required': False, 'allow_null': True},
                        'lastModifiedUser': {'required': False, 'allow_null': True, 'allow_blank': True},
                        'lastModifiedTimestamp': {'required': False, 'allow_null': True},
                        'downloadMLX': {'required': False, 'allow_null': True},
                        'excelInspectUploaded': {'required': False, 'allow_null': True},
                        'inspectionPictures': {'required': False, 'allow_null': True},
                        'postedSync': {'required': False, 'allow_null': True},
                        'formComplete': {'required': False, 'allow_null': True},
                        'concretePatchNeeded': {'required': False, 'allow_null': True},
                        'materialOrderNumberHD': {'required': False, 'allow_null': True, 'allow_blank': True},
                        'cpn_eta': {'required': False, 'allow_null': True},
                        'inspectionDueDates': {'required': False, 'allow_null': True},
                        'lastDateChecked': {'required': False, 'allow_null': True}}
        depth = 1
