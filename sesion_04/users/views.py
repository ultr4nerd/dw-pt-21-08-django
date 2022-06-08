"""Users app views"""

from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth import views as auth_views
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic as generic_views

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
    if request.user.is_authenticated:
        return redirect("music:show_songs")

    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("music:show_songs")
    return render(request, "users/signup.html", {"form": form})


class LoginView(auth_views.LoginView):
    template_name = "users/login.html"
    redirect_authenticated_user = True


class LogoutView(auth_views.LogoutView):
    pass


class SignupView(generic_views.FormView):
    template_name = "users/signup.html"
    form_class = SignupForm
    success_url = reverse_lazy("music:show_songs")

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(self.success_url)
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)
