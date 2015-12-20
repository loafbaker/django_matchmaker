from django.contrib import admin

# Register your models here.

from .models import PositionMatch, EmployerMatch, LocationMatch

admin.site.register(PositionMatch)
admin.site.register(EmployerMatch)
admin.site.register(LocationMatch)