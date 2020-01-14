from django.contrib import admin
from .models import CustomText, HomePage

admin.site.register(HomePage)
admin.site.register(CustomText)

# Register your models here.
