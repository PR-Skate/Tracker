from django.conf.urls import url
from django.urls import include
from rest_framework import routers

from .views import *

router = routers.DefaultRouter()
router.register(r'LocationInStore', LocationInStoreView, basename='LocationInStore')
router.register(r'ScopeOfWork', ScopeOfWorkView, basename='ScopeOfWork')
router.register(r'ScopeOfWorkStatus', ScopeOfWorkStatusView, basename='ScopeOfWorkStatus')
router.register(r'SchedulingWork', SchedulingWorkView, basename='SchedulingWork')
router.register(r'OrderMaterial', OrderMaterialView, basename='OrderMaterial')
router.register(r'MaterialList', MaterialListView, basename='MaterialList')
router.register(r'MaterialItem', MaterialItemView, basename='MaterialItem')
router.register(r'WorkOrderStatus', WorkOrderStatusView, basename='WorkOrderStatus')
router.register(r'WorkOrder', WorkOrderView, basename='WorkOrder')
router.register(r'Employee', EmployeeView, basename='Employee')
router.register(r'ArticleNumber', ArticleNumberView, basename='ArticleNumber')
router.register(r'LaborItem', LaborItemView, basename='LaborItem')
router.register(r'ArticleNumberState', ArticleNumberStateView, basename='ArticleNumberState')
router.register(r'Store', StoreView, basename='Store')
router.register(r'RegionCode', RegionCodeView, basename='RegionCode')
router.register(r'Customer', CustomerView, basename='Customer')
router.register(r'MicroRegionCode', MicroRegionCodeView, basename='MicroRegionCode')
router.register(r'PrepWork', PrepWorkView, basename='PrepWork')
urlpatterns = [
    url(r'^api/', include(router.urls)),
]