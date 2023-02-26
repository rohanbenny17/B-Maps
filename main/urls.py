from . import views
from django.urls import path


app_name = "main"
urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("login/employee", views.emp_login, name="emp_login"),
    path("login/user", views.user_login, name="user_login"),
    path("register", views.register, name="register"),
    path("reset", views.reset, name="reset")
]