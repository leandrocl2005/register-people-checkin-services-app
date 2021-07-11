from django.urls import path
from .views import (checkins_pacients_close, checkins_pacients_list,
                    checkins_pacients_edit, checkins_pacients_create,
                    checkins_companions_list, checkins_others_list,
                    checkins_others_edit, checkins_others_create,
                    checkins_others_close, checkins_change_companion)

urlpatterns = [
    # pacients
    path('pacientes/', checkins_pacients_list),
    path('pacientes/<int:pk>/editar/', checkins_pacients_edit),
    path('pacientes/cadastrar/', checkins_pacients_create),
    path('pacientes/<int:pk>/fechar/', checkins_pacients_close),
    # companions
    path('acompanhantes/', checkins_companions_list),
    # outros
    path('outros/', checkins_others_list),
    path('outros/<int:pk>/editar/', checkins_others_edit),
    path('outros/cadastrar/', checkins_others_create),
    path('outros/<int:pk>/fechar/', checkins_others_close),
    # change companion
    path('trocar_acompanhante/', checkins_change_companion)
]
