"""Users app URL configuration"""

from django.urls import path

from . import views

app_name = "users"
urlpatterns = [
    path("", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("signup", views.signup, name="signup"),
]
