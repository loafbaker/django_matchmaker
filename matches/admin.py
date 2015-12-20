from django.contrib import admin

# Register your models here.

from .models import JobMatch, EmployerMatch, LocationMatch

admin.site.register(JobMatch)
admin.site.register(EmployerMatch)
admin.site.register(LocationMatch)