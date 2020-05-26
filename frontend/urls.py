from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('customerForm', views.customerForm),
    path('employeeForm', views.employeeForm),
    path('prepWorkForm', views.prepWorkForm),
    path('sowForm', views.sowForm),
    path('workOrderForm',  views.workOrderForm),
    path('storeForm', views.storeForm),
    path('sign-in', views.signin),
    path('logout', views.signout)
]
