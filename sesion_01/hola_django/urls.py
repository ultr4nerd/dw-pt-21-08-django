"""hola_django URL Configuration"""

from django.contrib import admin
from django.urls import path

from mi_aplicacion.views import hola_mundo, suma

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hola_mundo),
    path('suma/', suma),
]
