from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "main/index.html")


def about(request):
    return render(request, "main/about.html")


def emp_login(request):
    if request.method == "POST":
        pass

    return render(request, "main/emp_login.html")


def user_login(request):
    if request.method == "POST":
        pass

    return render(request, "main/user_login.html")


def register(request):
    return render(request, "main/register.html")


def reset(request):
    return render(request, "main/reset.html")