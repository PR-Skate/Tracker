from __future__ import unicode_literals

from rest_framework_mongoengine.viewsets import ModelViewSet as MongoModelViewSet

from .serializers import *


class BasicView(MongoModelViewSet):
    serializer_class = BaseSerializer

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.serializer = self.__class__.serializer_class
        self.model = self.serializer.Meta.model

    def get_queryset(self):
        return self.model.objects.filter(**self.request.query_params.dict())


class LocationInStoreView(BasicView):
    serializer_class = LocationInStoreSerializer


class ScopeOfWorkView(BasicView):
    serializer_class = ScopeOfWorkSerializer


class ScopeOfWorkStatusView(BasicView):
    serializer_class = ScopeOfWorkStatusSerializer


class SchedulingWorkView(BasicView):
    serializer_class = SchedulingWorkSerializer


class OrderMaterialView(BasicView):
    serializer_class = OrderMaterialSerializer


class MaterialListView(BasicView):
    serializer_class = MaterialListSerializer


class MaterialItemView(BasicView):
    serializer_class = MaterialItemSerializer


class WorkOrderStatusView(BasicView):
    serializer_class = WorkOrderStatusSerializer


class WorkOrderView(BasicView):
    serializer_class = WorkOrderSerializer


class EmployeeView(BasicView):
    serializer_class = EmployeeSerializer


class ArticleNumberView(BasicView):
    serializer_class = ArticleNumberSerializer


class LaborItemView(BasicView):
    serializer_class = LaborItemSerializer


class ArticleNumberStateView(BasicView):
    serializer_class = ArticleNumberStateSerializer


class StoreView(BasicView):
    serializer_class = StoreSerializer


class RegionCodeView(BasicView):
    serializer_class = RegionCodeSerializer


class CustomerView(BasicView):
    serializer_class = CustomerSerializer


class MicroRegionCodeView(BasicView):
    serializer_class = MicroRegionCodeSerializer


class PrepWorkView(BasicView):
    serializer_class = PrepWorkSerializer
