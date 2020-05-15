from rest_framework_mongoengine import generics as drfme_generics

from .serializers import *


# Create your views here.


class WorkOrderStatusCreate(drfme_generics.ListCreateAPIView):
    queryset = WorkOrderStatus.objects.all()
    serializer_class = WorkOrderStatusSerializer


class StoreCreate(drfme_generics.ListCreateAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer


class CustomerCreate(drfme_generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class EmployeeCreate(drfme_generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
