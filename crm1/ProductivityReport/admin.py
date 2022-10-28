from django.contrib import admin

# Register your models here.

from .models import *
admin.site.register(CategoryOfDeployment)
admin.site.register(ProductivityReport)
admin.site.register(ProductivityNightReport)
