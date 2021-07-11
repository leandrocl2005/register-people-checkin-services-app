from django.urls import path
from .views import (people_list, person_create, person_edit)

urlpatterns = [
    path('', people_list),
    path('cadastrar/', person_create),
    path('<int:pk>/editar/', person_edit)
]
