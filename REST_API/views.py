from .serializers import WorkOrderStatusSerializer
from .serializers import StoreSerializer
from .serializers import *
from rest_framework_mongoengine import generics as drfme_generics
from Class_Types import *
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
