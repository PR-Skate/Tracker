from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index),
    path('customerForm', views.customer_form),
    url(r'^customerForm/(?P<id>\w+)$', views.customer_form, name='id'),

    path('employeeForm', views.employee_form),
    url(r'^employeeForm/(?P<id>\w+)$', views.employee_form, name='id'),

    path('prepWorkForm', views.prep_work_form),
    url(r'^prepWorkForm/(?P<id>\w+)$', views.prep_work_form, name='id'),

    path('workOrderForm', views.work_order_form),
    url(r'^workOrderForm/(?P<id>\w+)$', views.work_order_form, name='id'),

    path('storeForm', views.store_form),
    url(r'^storeForm/(?P<id>\w+)$', views.store_form, name='id'),

    path('microRegionCodeForm', views.micro_region_form),
    url(r'^microRegionCodeForm/(?P<id>\w+)$', views.micro_region_form, name='id'),

    path('regionCodeForm', views.region_form),
    url(r'^regionCodeForm/(?P<id>\w+)$', views.region_form, name='id'),

    path('workOrderStatusForm', views.work_order_status_form),
    url(r'^workOrderStatusForm/(?P<id>\w+)$', views.work_order_status_form, name='id'),

    path('sowForm', views.scope_of_work_form),
    url(r'^sowForm/(?P<id>\w+)$', views.scope_of_work_form, name='id'),

    path('sowStatusForm', views.scope_of_work_status_form),
    url(r'^sowStatusForm/(?P<id>\w+)$', views.scope_of_work_status_form, name='id'),

    path('laborItemForm', views.labor_item_form),
    url(r'^laborItemForm/(?P<id>\w+)$', views.labor_item_form, name='id'),

    path('articleNumberStateForm', views.article_number_state_form),
    url(r'^articleNumberStateForm/(?P<id>\w+)$', views.article_number_state_form, name='id'),

    path('articleNumberForm', views.article_number_form),
    url(r'^articleNumberForm/(?P<id>\w+)$', views.article_number_form, name='id'),

    path('materialItemForm', views.material_item_form),
    url(r'^materialItemForm/(?P<id>\w+)$', views.material_item_form, name='id'),

    path('locationInStoreForm', views.location_in_store_form),
    url(r'^locationInStoreForm/(?P<id>\w+)$', views.location_in_store_form, name='id'),

    path('orderMaterialForm', views.order_material_form),
    url(r'^orderMaterialForm/(?P<id>\w+)$', views.order_material_form, name='id'),

    path('sign-in', views.signin),
    path('logout', views.signout),
    path('customerReport', views.customer_report),
    path('employeeReport', views.employee_report),
    path('sowReport', views.scope_of_work_report),
    path('storeReport', views.store_report),
    path('workOrderReport', views.work_order_report),
    path('articleNumberReport', views.article_number_report),
    path('articleNumberStateReport', views.article_number_state_report),
    path('laborItemReport', views.labor_item_report),
    path('materialItemReport', views.material_item_report),
    path('materialListReport', views.material_list_report),
    path('orderMaterialReport', views.order_material_report),
    path('locationInStoreReport', views.location_in_store_report),
    path('sowStatusReport', views.scope_of_work_status_report),
    path('microRegionCodeReport', views.micro_region_code_report),
    path('regionCodeReport', views.region_code_report),
    path('workOrderStatusReport', views.work_order_status_report),
    path('prepWorkReport', views.prep_work_report),
    path('schedulingWorkReport', views.scheduling_work_report)
]
