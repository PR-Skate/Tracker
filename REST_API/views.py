from .serializers import WorkOrderStatusSerializer
from rest_framework_mongoengine import generics as drfme_generics
from Class_Types import *
# Create your views here.


class WorkOrderStatusCreate(drfme_generics.ListCreateAPIView):
    queryset = WorkOrderStatus.objects.all()
    serializer_class = WorkOrderStatusSerializer
