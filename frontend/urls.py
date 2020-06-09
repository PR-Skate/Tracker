from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('customerForm', views.customer_form),
    path('employeeForm', views.employee_form),
    path('prepWorkForm', views.prep_work_form),
    path('workOrderForm', views.work_order_form),
    path('storeForm', views.store_form),
    path('microRegionCodeForm', views.micro_region_form),
    path('regionCodeForm', views.region_form),
    path('workOrderStatusForm', views.work_order_status_form),
    path('scopeOfWorkStatusForm', views.scope_of_work_status_form),
    path('laborItemForm', views.labor_item_form),
    path('articleNumberStateForm', views.article_number_state_form),
    path('articleNumberForm', views.article_number_form),
    path('materialItemForm', views.material_item_form),
    path('materialListForm', views.material_list_form),
    path('locationInStoreForm', views.location_in_store_form),

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
