from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('customerForm', views.customerForm),
    path('employeeForm', views.employeeForm),
    path('prepWorkForm', views.prepWorkForm),
    path('sowForm', views.sowForm),
    path('workOrderForm', views.workOrderForm),
    path('storeForm', views.storeForm),
    path('sign-in', views.signin),
    path('logout', views.signout),
    path('customerReport', views.customerReport),
    path('employeeReport', views.employeeReport),
    path('sowReport', views.sowReport),
    path('storeReport', views.storeReport),
    path('workOrderReport', views.workOrderReport),
    path('articleNumberReport', views.articleNumberReport),
    path('articleNumberStateReport', views.articleNumberStateReport),
    path('laborItemReport', views.laborItemReport),
    path('materialItemReport', views.materialItemReport),
    path('materialListReport', views.materialListReport),
    path('orderMaterialReport', views.orderMaterialReport),
    path('locationInStoreReport', views.locationInStoreReport),
    path('sowStatusReport', views.sowStatusReport),
    path('microRegionCodeReport', views.microRegionCodeReport),
    path('regionCodeReport', views.regionCodeReport),
    path('workOrderStatusReport', views.workOrderStatusReport),
    path('prepWorkReport', views.prepWorkReport),
    path('schedulingWorkReport', views.schedulingWorkReport)
]
