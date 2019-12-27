from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.shortcuts import render

from . import models

admin.site.register(models.User)