from django.db import models
from django.contrib.auth.models import AbstractUser

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
    skills = models.TextField(null=True, blank=True)     # Delimiter separated 
    location=models.TextField(null=True, blank=True,help_text="Tell us in which city do you live")
    contact_number = models.PositiveIntegerField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)
    github = models.URLField(null=True, blank=True)
    upvotes = models.ManyToManyField('Lightbulb', related_name="upvoters")
    downvotes = models.ManyToManyField('Lightbulb', related_name="downvoters")
    stars = models.ManyToManyField('Lightbulb', related_name="starrers")
    timestamp=models.DateTimeField(auto_now_add=True)#for how long the user has been using lightbulbs
    
    
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

    def __str__(self):
        return f"{self.creator} - {self.title}"


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