from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Employer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length = 30)


@receiver(post_save, sender=User)
def create_employer(sender, instance, created, **kwargs):
    if created:
        Employer.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_employer(sender, instance, **kwargs):
    instance.employer.save()

class Job(models.Model):
    poster = models.ForeignKey(Employer, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=50)
    establishment_name = models.CharField(max_length = 50)
    address = models.CharField(max_length = 50)
    state = models.CharField(max_length = 20)
    zip_code = models.CharField(max_length = 10)

