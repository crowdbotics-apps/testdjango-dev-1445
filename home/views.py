from django.views.generic import CreateView, UpdateView, DetailView, ListView
from django.shortcuts import render
from .models import Test, Table, TestDemo, CustomText, HomePage, Testdemo1


def home(request):
    packages = [
        {
            "name": "django-file-upload",
            "url": "http://pypi.python.org/pypi/django-file-upload/1.0.0",
        },
        {
            "name": "django-allauth",
            "url": "https://pypi.org/project/django-allauth/0.38.0/",
        },
        {
            "name": "django-bootstrap4",
            "url": "https://pypi.org/project/django-bootstrap4/0.0.7/",
        },
        {
            "name": "djangorestframework",
            "url": "https://pypi.org/project/djangorestframework/3.9.0/",
        },
    ]
    context = {
        "customtext": CustomText.objects.first(),
        "homepage": HomePage.objects.first(),
        "packages": packages,
    }
    return render(request, "home/index.html", context)
