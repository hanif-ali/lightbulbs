from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class LBUser(AbstractUser):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    description = models.CharField(max_length=30, blank=True)
    profession = models.CharField(max_length=30, blank=True)
    bio = models.TextField(null=True, blank=True)
    age = models.PositiveSmallIntegerField()
    skills = models.TextField(null=True, blank=True)     # Delimiter separated Values
    contact_number = models.PositiveIntegerField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)
    github = models.URLField(null=True, blank=True)
    
    
    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "LBUser"
