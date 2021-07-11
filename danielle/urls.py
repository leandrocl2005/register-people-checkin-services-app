from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from people.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('pessoas/', include('people.urls')),
    path('checkins/', include('checkin.urls')),
    path(
        'servicos-da-casa/',
        include('houseservices.urls', namespace="houseservices"),
    ),
    path('users/', include('users.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('', home)
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
