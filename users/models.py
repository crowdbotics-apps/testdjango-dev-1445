from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    name = models.CharField(null=True, blank=True, max_length=255,)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})


class Demo(models.Model):
    "Generated Model"
    demo = models.DateField(auto_now=False, auto_now_add=False,)
    demotest = models.DecimalField(
        null=True, blank=True, max_digits=30, decimal_places=10,
    )
