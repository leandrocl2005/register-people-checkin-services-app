from django.urls import path

from .views import user_profile_detail

urlpatterns = [path('profile/', user_profile_detail)]
