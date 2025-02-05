from django.db import models
from django.auth.models import AbstractUser
# Create your models here.

class participant(AbstractUser):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

class event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True,blank=True)
    date = models.DateField()
    time = models.TimeField(null=True,blank=True)
    rules_and_regulations = models.TextField(null=True,blank=True)
    venue = models.CharField(max_length=100,null=True,blank=True)
    image = models.ImageField(upload_to='event_registration/images',null=True,blank=True)

    def __str__(self):
        return self.name
    
class organizer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    event = models.ForeignKey(event,on_delete=models.CASCADE)

    def __str__(self):
        return self.name