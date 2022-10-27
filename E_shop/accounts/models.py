from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    porfolio = models.URLField(null=True, blank=True)
    image = models.ImageField(upload_to='users/', default='users/noavatar.png')

    def __str__(self):
        return self.user.username