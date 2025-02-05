from django.db import models

# Create your models here.

class event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True,blank=True)
    date = models.DateField()
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