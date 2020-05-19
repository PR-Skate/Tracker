from __future__ import unicode_literals

from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework_mongoengine.generics import GenericAPIView
from rest_framework_mongoengine.viewsets import ModelViewSet as MongoModelViewSet
from .serializers import *


class BasicView(MongoModelViewSet):
    serializer_class = LocationInStoreSerializer
    look_up = 'id'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.serializer = self.__class__.serializer_class
        self.model = self.serializer.Meta.model

    def get(self, request, format=None):
        model_instances = self.model.objects.all()
        serializer = self.serializer(model_instances, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = self.serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_object(self, pk):
        try:
            return self.model.objects.get(pk=pk)
        except self.model.DoesNotExist:
            raise Http404

    def get_object(self):
        return GenericAPIView.get_object(self)

    def get(self, request, pk, format=None):
        model_instance = self.get_object(pk)
        serializer = self.serializer(model_instance)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        model_instance = self.get_object(pk)
        serializer = self.serializer(model_instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        model_instance = self.get_object(pk)
        model_instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_queryset(self):
        return self.model.objects.filter(**self.request.query_params.dict())


class LocationInStoreView(BasicView):
    look_up = 'id'
    serializer_class = LocationInStoreSerializer

    def get_queryset(self):
        return LocationInStore.objects.all()


class ScopeOfWorkView(BasicView):
    look_up = 'id'
    serializer_class = ScopeOfWorkSerializer

    def get_queryset(self):
        return ScopeOfWork.objects.all()


class ScopeOfWorkStatusView(BasicView):
    look_up = 'id'
    serializer_class = ScopeOfWorkStatusSerializer

    def get_queryset(self):
        return ScopeOfWorkStatus.objects.all()


class SchedulingWorkView(BasicView):
    look_up = 'id'
    serializer_class = SchedulingWorkSerializer

    def get_queryset(self):
        return SchedulingWork.objects.all()


class OrderMaterialView(BasicView):
    look_up = 'id'
    serializer_class = OrderMaterialSerializer

    def get_queryset(self):
        return OrderMaterial.objects.all()


class MaterialListView(BasicView):
    look_up = 'id'
    serializer_class = MaterialListSerializer

    def get_queryset(self):
        return MaterialList.objects.all()


class MaterialItemView(BasicView):
    look_up = 'id'
    serializer_class = MaterialItemSerializer

    def get_queryset(self):
        return MaterialItem.objects.all()


class WorkOrderStatusView(BasicView):
    look_up = 'id'
    serializer_class = WorkOrderStatusSerializer

    def get_queryset(self):
        return WorkOrderStatus.objects.all()


class WorkOrderView(BasicView):
    look_up = 'id'
    serializer_class = WorkOrderSerializer

    def get_queryset(self):
        return WorkOrder.objects.all()


class EmployeeView(BasicView):
    look_up = 'id'
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        return Employee.objects.all()


class ArticleNumberView(BasicView):
    look_up = 'id'
    serializer_class = ArticleNumberSerializer

    def get_queryset(self):
        return ArticleNumber.objects.all()


class LaborItemView(BasicView):
    look_up = 'id'
    serializer_class = LaborItemSerializer

    def get_queryset(self):
        return LaborItem.objects.all()


class ArticleNumberStateView(BasicView):
    look_up = 'id'
    serializer_class = ArticleNumberStateSerializer

    def get_queryset(self):
        return ArticleNumberState.objects.all()


class StoreView(BasicView):
    look_up = 'id'
    serializer_class = StoreSerializer

    def get_queryset(self):
        return Store.objects.all()


class RegionCodeView(BasicView):
    look_up = 'id'
    serializer_class = RegionCodeSerializer

    def get_queryset(self):
        return RegionCode.objects.all()


class CustomerView(BasicView):
    look_up = 'id'
    serializer_class = CustomerSerializer


class MicroRegionCodeView(BasicView):
    look_up = 'id'
    serializer_class = MicroRegionCodeSerializer

    def get_queryset(self):
        return MicroRegionCode.objects.all()


class PrepWorkView(BasicView):
    look_up = 'id'
    serializer_class = PrepWorkSerializer

    def get_queryset(self):
        return PrepWork.objects.all()
