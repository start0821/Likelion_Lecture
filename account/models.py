from django.db import models
from django.contrib.auth.models import User

# Create your models here.
def file_path(instance, filename):
    return '{0}/{1}'.format(instance.user.username,filename)

class Profile(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE)
    image = models.ImageField(upload_to=file_path)
