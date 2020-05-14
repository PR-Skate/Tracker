from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('storeForm', views.storeForm),
    path('sowForm', views.sowForm),
    path('workOrderform', views.workOrderform),
    path('customerForm', views.customerForm)

]
