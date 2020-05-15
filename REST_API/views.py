from rest_framework_mongoengine import generics as drfme_generics
from .serializers import *
# Create your views here.


class LocationInStoreCreate(drfme_generics.ListCreateAPIView):
    queryset = LocationInStore.objects.all()
    serializer_class = LocationInStoreSerializer


class ScopeOfWorkCreate(drfme_generics.ListCreateAPIView):
    queryset = ScopeOfWork.objects.all()
    serializer_class = ScopeOfWorkSerializer


class ScopeOfWorkStatusCreate(drfme_generics.ListCreateAPIView):
    queryset = ScopeOfWorkStatus.objects.all()
    serializer_class = ScopeOfWorkStatusSerializer


class SchedulingWorkCreate(drfme_generics.ListCreateAPIView):
    queryset = SchedulingWork.objects.all()
    serializer_class = SchedulingWorkSerializer


class OrderMaterialCreate(drfme_generics.ListCreateAPIView):
    queryset = OrderMaterial.objects.all()
    serializer_class = OrderMaterialSerializer


class MaterialListCreate(drfme_generics.ListCreateAPIView):
    queryset = MaterialList.objects.all()
    serializer_class = MaterialListSerializer


class MaterialItemCreate(drfme_generics.ListCreateAPIView):
    queryset = MaterialItem.objects.all()
    serializer_class = MaterialItemSerializer


class WorkOrderStatusCreate(drfme_generics.ListCreateAPIView):
    queryset = WorkOrderStatus.objects.all()
    serializer_class = WorkOrderStatusSerializer


class WorkOrderCreate(drfme_generics.ListCreateAPIView):
    queryset = WorkOrder.objects.all()
    serializer_class = WorkOrderSerializer


class EmployeeCreate(drfme_generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class ArticleNumberCreate(drfme_generics.ListCreateAPIView):
    queryset = ArticleNumber.objects.all()
    serializer_class = ArticleNumberSerializer


class LaborItemCreate(drfme_generics.ListCreateAPIView):
    queryset = LaborItem.objects.all()
    serializer_class = LaborItemSerializer


class ArticleNumberStateCreate(drfme_generics.ListCreateAPIView):
    queryset = ArticleNumberState.objects.all()
    serializer_class = ArticleNumberStateSerializer


class StoreCreate(drfme_generics.ListCreateAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer


class RegionCodeCreate(drfme_generics.ListCreateAPIView):
    queryset = RegionCode.objects.all()
    serializer_class = RegionCodeSerializer


class CustomerCreate(drfme_generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class MicroRegionCodeCreate(drfme_generics.ListCreateAPIView):
    queryset = MicroRegionCode.objects.all()
    serializer_class = MicroRegionCodeSerializer


class PrepWorkCreate(drfme_generics.ListCreateAPIView):
    queryset = PrepWork.objects.all()
    serializer_class = PrepWorkSerializer


