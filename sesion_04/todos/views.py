from django.shortcuts import render

todos = []


def index(request):
    if request.method == "POST":
        new_todo = request.POST['new_todo']
        todos.append(new_todo)
    return render(request, "todos/index.html", {"todos": todos})
