from django.contrib import admin

# Register your models here.

from .models import enquery,apply

admin.site.register(enquery)
admin.site.register(apply)