from django.urls import path
from tenant_app.views import *

urlpatterns = [
    path("register/", register_tenant, name="register_name"),
]