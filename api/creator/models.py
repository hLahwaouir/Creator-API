from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()

def profile_image_uplaod_to(instance, filename):
    return 'user_{}/profile_image/{}'.format(instance.user.id, filename) 

def logo_url_uplaod_to(instance, filename):
    return 'user_{}/profile_image/{}'.format(instance.user.id, filename) 



class Domain(models.Model):
    name = models.CharField(max_length=150)
    is_verified = models.BooleanField(default=False)

class Creator(models.Model):
    domain = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    profile_image_url = models.ImageField(upload_to=profile_image_uplaod_to)
    logo_url = models.ImageField(upload_to=logo_url_uplaod_to, null=True)
    bio = models.TextField(null=True)
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    contry = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=50)
    industry = models.CharField(max_length=50)
    phon = models.CharField(max_length=20, null=True)
    domain = models.OneToOneField(Domain, on_delete=models.CASCADE, null=True)