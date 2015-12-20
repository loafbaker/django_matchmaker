from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from .models import Job, Location, Employer


@receiver(pre_save, sender=Job)
def pre_save_job(sender, instance, *args, **kwargs):
	instance.slug = slugify(instance.text)


@receiver(pre_save, sender=Location)
def pre_save_location(sender, instance, *args, **kwargs):
	instance.slug = slugify(instance.name)


@receiver(pre_save, sender=Employer)
def pre_save_employer(sender, instance, *args, **kwargs):
	instance.slug = slugify(instance.name + ' ' + instance.location.name)