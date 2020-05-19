from django.conf.urls import url
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns

from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'Customer', views.CustomerView, basename='Customer')

urlpatterns = [
    url(r'^api/', include(router.urls)),
]

