from django.contrib import admin
from .models import *
from .apps import MosConfig
# Register your models here.
admin.site.register(Person)