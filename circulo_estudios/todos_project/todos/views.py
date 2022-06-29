from django.views.generic import TemplateView

from rest_framework import viewsets

from .models import Todo
from .serializers import TodoSerializer


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer



class TodoTemplateView(TemplateView):
    template_name = "todos.html"
