from rest_framework import routers

from django.urls import re_path
from django.conf.urls.static import static
from django.conf import settings

from core import views

router = routers.DefaultRouter(trailing_slash=False)

urlpatterns = [
				re_path(r'^rpc/form/$', views.form_api),
				re_path(r'^rpc/form/([0-9]+)$', views.form_api)
]

