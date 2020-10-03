from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("register/", views.register, name="register"),
    path("logout/", views.logout_the_user, name="logout"),
    path("login/", views.login_the_user, name="login"),
]
