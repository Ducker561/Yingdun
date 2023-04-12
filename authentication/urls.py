from django.urls import path

from . import views

app_name = "authentication"
urlpatterns = [
    # ex: /authentication/
    path("", views.index, name="index"),
    # ex: /authentication/check_login/
    path("check_login/", views.login, name="login"),
    # ex: /authentication/register
    path("register/", views.register, name="register"),
    # ex: /authentication/register/register_user/
    path("register/register_user/", views.register_user, name="register_user"),
]