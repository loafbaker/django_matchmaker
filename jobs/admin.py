from django.contrib import admin

# Register your models here.
from .models import Job, Location, Employer

admin.site.register(Job)
admin.site.register(Location)
admin.site.register(Employer)
