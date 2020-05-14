from django.urls import path
from . import views

urlpatterns = [
    path('api/WorkOrderStatus/', views.WorkOrderStatusCreate.as_view()),
]