from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

class Profile(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=40, null=True)
    last_name = models.CharField(max_length=40, null=True)
    email = models.EmailField(max_length=140, null=True) # This doesn't seem right
    user_type = models.CharField(max_length=40, default='RBT')
    def __str__(self):
        return self.user.username



   
class Trainee(models.Model):
    #first_name = models.CharField(max_length=40)
    #last_name = models.CharField(max_length=40)
    alias = models.CharField(max_length=40, primary_key=True)
    age = models.IntegerField()
    trainers = models.ManyToManyField(Profile)

    # Trainee's program settings
    # !!! Need to update from Erica about preferences
    dry_checks = models.BooleanField(default=False)
    underwear = models.BooleanField(default=True)
    positive_practice = models.BooleanField(default=False)
    liquid_intake = models.BooleanField(default=False)

    
    # Information about Trainee's current state in training program
    current_voids = models.IntegerField(default=0)
    current_accidents = models.IntegerField(default=0)
    current_level = models.IntegerField(default=0)
    
    
    # Information about Trainee's history in program
    total_voids = models.IntegerField(default=0)
    total_accidents = models.IntegerField(default=0)

    def __str__(self):
        return self.alias 




