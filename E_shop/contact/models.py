from django.db import models
from django.utils import timezone

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    subject = models.CharField(max_length=264)
    message = models.TextField()
    send_day = models.DateField(default=timezone.now)
    def __str__(self):
        return self.subject
class StatusLocation(models.Model):
    name = models.CharField(max_length=150)


    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=150)

    email = models.EmailField()
    phone_number=models.CharField(max_length=20)
    link = models.URLField(null=True, blank=True)
    status_Location = models.ForeignKey(StatusLocation, on_delete=models.PROTECT)
    def __str__(self):
        return self.name

