from django.views.generic import CreateView, UpdateView, DetailView, ListView
from django.shortcuts import render
from .models import Test, Table, TestDemo, CustomText, HomePage, Testdemo1


def home(request):
    packages = [
	{'name':'chainer_addons', 'url': 'http://pypi.python.org/pypi/chainer_addons/0.1.3'},
	{'name':'blast-score-ratio', 'url': 'http://pypi.python.org/pypi/blast-score-ratio/1.0.6'},
	{'name':'chainercv', 'url': 'http://pypi.python.org/pypi/chainercv/0.8.0'},
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
