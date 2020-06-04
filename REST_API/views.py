from __future__ import unicode_literals

from django.contrib.auth import login
from knox.views import LoginView as KnoxLoginView
from rest_framework import permissions
from rest_framework.authentication import BasicAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.response import Response
from rest_framework_mongoengine.viewsets import ModelViewSet as MongoModelViewSet

from .serializers import *


class LoginView(KnoxLoginView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [permissions.AllowAny]

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginView, self).post(request, format=None)


class BasicView(MongoModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = LocationInStoreSerializer

    def __init__(self, **kwargs):
        MongoModelViewSet().__init__(**kwargs)
        self.serializer = self.__class__.serializer_class
        self.model = self.serializer.Meta.model

        self.queryset = self.model.objects.all()

    def get_queryset(self):
        if hasattr(self, 'request'):
            return self.model.objects.filter(**self.request.query_params.dict())
        else:
            return self.model.objects.all()

    def retrieve(self, request, *args, **kwargs):
        print(request.user)
        return MongoModelViewSet.retrieve(self, request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        instance = queryset.get(id=kwargs.get('id'))
        request.data.update({'lastModifiedUser': request.user.username})
        instance.update(**request.data)
        return Response('Updated')

    def create(self, request, *args, **kwargs):
        print(request.user)
        request.data.update({'createdUser': request.user.username})
        return MongoModelViewSet.create(self, request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return MongoModelViewSet.destroy(self, request, *args, **kwargs)


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
