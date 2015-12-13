from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UserJob
from jobs.models import Job, Location, Employer


@receiver(post_save, sender=UserJob)
def post_save_user_job(sender, instance, created, *args, **kwargs):
    job = instance.position.lower()
    location = instance.location.lower()
    employer_name = instance.employer_name.lower()
    new_job, job_created = Job.objects.get_or_create(text=job) # case insensitive
    new_location, location_created = Location.objects.get_or_create(name=location)
    new_employer, employer_created = Employer.objects.get_or_create(location=new_location, name=employer_name)
