from django.conf import settings
from django.db import models
from django.urls import reverse

# Create your models here.

User = settings.AUTH_USER_MODEL


def upload_location(instance,filename):
    location = str(instance.user.username)
    return '%s/%s' % (location, filename)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=120, null=True, blank=True)
    picture = models.ImageField(upload_to=upload_location, null=True, blank=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        url = reverse('profile', kwargs={'username':self.user.username})
        return url

    def like_link(self):
        url = reverse('like_user', kwargs={'id': self.user.id})
        return url


class UserJob(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    position = models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    employer_name = models.CharField(max_length=250)

    def __str__(self):
        return self.position
