"""Global Napster URL Configuration"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("todos/", include("todos.urls")),
    path("music/", include("music.urls")),
    path("", include("users.urls")),
]
