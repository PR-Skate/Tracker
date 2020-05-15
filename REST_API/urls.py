from django.urls import path
from . import views
urlpatterns = [
    path('api/LocationInStore/', views.LocationInStoreCreate.as_view()),
    path('api/ScopeOfWork/', views.ScopeOfWorkCreate.as_view()),
    path('api/ScopeOfWorkStatus/', views.ScopeOfWorkStatusCreate.as_view()),
    path('api/SchedulingWork/', views.SchedulingWorkCreate.as_view()),
    path('api/OrderMaterial/', views.OrderMaterialCreate.as_view()),
    path('api/MaterialList/', views.MaterialListCreate.as_view()),
    path('api/MaterialItem/', views.MaterialItemCreate.as_view()),
    path('api/WorkOrderStatus/', views.WorkOrderStatusCreate.as_view()),
    path('api/WorkOrder/', views.WorkOrderCreate.as_view()),
    path('api/Employee/', views.EmployeeCreate.as_view()),
    path('api/ArticleNumber/', views.ArticleNumberCreate.as_view()),
    path('api/LaborItem/', views.LaborItemCreate.as_view()),
    path('api/ArticleNumberState/', views.ArticleNumberStateCreate.as_view()),
    path('api/Store/', views.StoreCreate.as_view()),
    path('api/RegionCode/', views.RegionCodeCreate.as_view()),
    path('api/Customer/', views.CustomerCreate.as_view()),
    path('api/MicroRegionCode/', views.MicroRegionCodeCreate.as_view()),
    path('api/PrepWork/', views.PrepWorkCreate.as_view()),
]