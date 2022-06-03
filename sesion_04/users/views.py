"""Users app views"""

from django.contrib.auth import get_user_model, authenticate, login, logout
from django.shortcuts import redirect, render

from .forms import SignupForm


User = get_user_model()


def login_view(request):
    if request.user.is_authenticated:
        return redirect("music:show_songs")

    context = {}

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if not user:
            context["error"] = "Credenciales inválidas"
        else:
            login(request, user)
            next_url = request.GET.get("next")
            return redirect(next_url if next_url else "music:show_songs")

    return render(request, "users/login.html", context)


def logout_view(request):
    logout(request)
    return redirect("users:login")


def signup(request):
    form = SignupForm()

    if request.method == 'POST':
        form = SignupForm(request.POST)
        form.is_valid()
    return render(request, "users/signup.html", {"form": form})
