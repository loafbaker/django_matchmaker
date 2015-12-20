from django.db import models

# Create your models here.
from django.conf import settings
from localflavor.us.models import USStateField

User = settings.AUTH_USER_MODEL

class Job(models.Model):
    text = models.CharField(max_length=120, unique=True)
    slug = models.SlugField()
    active = models.BooleanField(default=True)
    flagged = models.ManyToManyField(User, blank=True) # warning
    #users = models.ManyToManyField(User, null=True, blank=True)

    def __unicode__(self):
        return self.text


class Location(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField()
    active = models.BooleanField(default=True)
    flagged = models.ManyToManyField(User, blank=True) # warning

    def __unicode__(self):
        return self.name


class Employer(models.Model):
    name = models.CharField(max_length=250)
    location = models.ForeignKey(Location, null=True, blank=True)
    slug = models.SlugField()
    # state = USStateField(null=True, blank=True)
    # website, lat_lang, etc.

    def __unicode__(self):
        return self.name

    class Meta:
        unique_together = ('name', 'location')

