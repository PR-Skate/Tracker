from django.urls import path
from . import views

urlpatterns = [
    path('api/WorkOrderStatus/', views.WorkOrderStatusCreate.as_view()),
    path('api/Store/', views.StoreCreate.as_view()),
    path('api/Customer/', views.CustomerCreate.as_view()),
]