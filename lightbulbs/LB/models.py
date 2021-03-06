from django.db import models
from django.contrib.auth.models import AbstractUser
from .rating import getRating
import time
from django.urls import reverse

# Create your models here.


class LBUser(AbstractUser):
    """LightBulb User Model. Extends the default django User Model to act as an
    Authentication Model. Additional Fields are defined"""



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
    upvotes = models.ManyToManyField('Lightbulb', related_name="upvoters")
    downvotes = models.ManyToManyField('Lightbulb', related_name="downvoters")
    stars = models.ManyToManyField('Lightbulb', related_name="starrers")
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "LBUser"


class Lightbulb(models.Model):
    """Model for Individual Ideas"""

    creator = models.ForeignKey(LBUser, on_delete=models.CASCADE, related_name='lightbulbs')
    timestamp = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=50)
    description = models.TextField()
    category = models.CharField(max_length=20)
    rating = models.DecimalField( decimal_places=6,max_digits=12, null=True)
    
    def save(self, *args, **kwargs):
        super(Lightbulb, self).save(*args, **kwargs)
        self.rating = getRating(self.upvoters.count(), self.downvoters.count(), self.timestamp)
        super(Lightbulb, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.creator} - {self.title}"

    def get_absolute_url(self):
        return reverse("idea", kwargs={"id_number": self.id})
    


class Proposal(models.Model):
    """Model for Proposals sent by users for participating in an idea"""
    
    sender = models.ForeignKey(LBUser, on_delete=models.CASCADE, related_name="sent_proposals")
    lightbulb = models.ForeignKey(Lightbulb, on_delete=models.CASCADE, related_name="proposals")
    timestamp = models.DateTimeField(auto_now_add=True)
    message = models.TextField()

    def __str__(self):
        return f"Proposal from {self.sender} for {self.lightbulb.title}"


class Message(models.Model):
    """Model for messages"""
    
    sender = models.ForeignKey(LBUser, on_delete=models.CASCADE, related_name="sent_messages")
    receiver = models.ForeignKey(LBUser, on_delete=models.CASCADE, related_name="received_messages")
    timestamp = models.DateTimeField(auto_now_add=True)
    message = models.TextField()


    def __str__(self):
        return f"{self.sender} - {self.message}"


class Notification(models.Model):
    """Model for notifications. Includes a link which is the page that the app will go to 
    upon clicking that link"""

    user = models.ForeignKey(LBUser, on_delete=models.CASCADE, related_name="notifications")
    message = models.CharField(max_length=50)
    link = models.URLField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.message}"