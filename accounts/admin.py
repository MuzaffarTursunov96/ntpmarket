from atexit import register
from django.contrib import admin

# Register your models here.
from accounts.models import *
admin.site.register(User)