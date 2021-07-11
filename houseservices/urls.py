from django.urls import path
from .views import (house_services_create, house_services_delete,
                    house_services_edit, house_services_list)

app_name = 'houseservices'

urlpatterns = [
    path('', house_services_list, name='list'),
    path('registrar/', house_services_create, name='create'),
    path('<int:pk>/editar/', house_services_edit, name='detail'),
    path('<int:pk>/deletar/', house_services_delete, name='delete')
]
