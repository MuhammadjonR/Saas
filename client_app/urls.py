from django.urls import path 

from .views import index, create_tenant

urlpatterns = [
    path('', index, name="client_index"),
    path('create_employee', create_tenant, name="create_employee")
]