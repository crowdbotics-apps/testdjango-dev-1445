from django.views.generic import CreateView, UpdateView, DetailView, ListView
from django.shortcuts import render
from .models import Test, Table, TestDemo, CustomText, HomePage, Testdemo1


def home(request):
    packages = [
	{'name':'blast-score-ratio', 'url': 'http://pypi.python.org/pypi/blast-score-ratio/1.0.6'},
	{'name':'chainercv', 'url': 'http://pypi.python.org/pypi/chainercv/0.8.0'},
	{'name':'blaz', 'url': 'http://pypi.python.org/pypi/blaz/0.0.25'},
	{'name':'blaster', 'url': 'http://pypi.python.org/pypi/blaster/0.1.5'},
	{'name':'BlastRadius', 'url': 'http://pypi.python.org/pypi/BlastRadius/0.1.6'},
	{'name':'blasy', 'url': 'http://pypi.python.org/pypi/blasy/0.1.2'},
	{'name':'blastbesties', 'url': 'http://pypi.python.org/pypi/blastbesties/1.1.1'},
	{'name':'blargs', 'url': 'http://pypi.python.org/pypi/blargs/0.2.29b'},
	{'name':'blargparse', 'url': 'http://pypi.python.org/pypi/blargparse/0.0.3'},
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
