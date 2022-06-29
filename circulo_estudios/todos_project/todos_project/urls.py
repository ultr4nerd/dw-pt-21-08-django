"""todos_project URL Configuration"""

from rest_framework import routers

from django.contrib import admin
from django.urls import path

from todos.views import TodoViewSet, TodoTemplateView

router = routers.SimpleRouter()
router.register(r'todos', TodoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", TodoTemplateView.as_view()),
] + router.urls
