from django.urls import path
from . import views

urlpatterns = [
    path('api/WorkOrderStatus/', views.WorkOrderStatusCreate.as_view()),
    path('api/Employee/', views.EmployeeCreate.as_view()),
]