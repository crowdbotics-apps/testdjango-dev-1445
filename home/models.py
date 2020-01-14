from django.conf import settings
from django.db import models

# Create your models here.

from django.db import models


class CustomText(models.Model):
    title = models.CharField(max_length=150,)
    test = models.BinaryField(null=True, blank=True,)

    def __str__(self):
        return self.title

    @property
    def api(self):
        return f"/api/v1/customtext/{self.id}/"

    @property
    def field(self):
        return "title"


class HomePage(models.Model):
    body = models.TextField()
    testdata = models.CharField(null=True, blank=True, max_length=356,)
    demo = models.CharField(null=True, blank=True, max_length=256,)

    @property
    def api(self):
        return f"/api/v1/homepage/{self.id}/"

    @property
    def field(self):
        return "body"


class Test(models.Model):
    "Generated Model"
    test = models.TextField()


class Testdemo1(models.Model):
    "Generated Model"
    tes = models.SmallIntegerField()


class TestDemo(models.Model):
    "Generated Model"
    design = models.BigIntegerField()


class Table(models.Model):
    "Generated Model"
    column = models.TextField()


class UI(models.Model):
    "Generated Model"
    ui = models.CharField(max_length=257,)
