"""Lista app URL's config"""

from django.urls import path

from lista.views import mostrar_listas, crear_lista, mostrar_lista

app_name = "lista"
urlpatterns = [
    path("mostrar/", mostrar_listas, name="mostrar_listas"),  # lista:mostrar_listas
    path("crear/", crear_lista, name="crear_lista"),  # lista:crear_lista
    path("mostrar/<str:nombre>", mostrar_lista, name="mostrar_lista")  # lista:mostrar_lista
]
