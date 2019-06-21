from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class Profile(models.Model):
    """
    Class that contains Profile details
    """
    dp = models.ImageField(upload_to = 'images/', blank=True)
    bio = models.TextField()
    contact = models.CharField(max_length = 30, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    post_save.connect(save_user_profile, sender=User)

    def save_profile(self):
        self.save()

    def del_profile(self):
        self.delete()

    @classmethod
    def get_by_id(cls, user_id):
            profile = Profile.objects.get(user_id = user_id)
            return profile

    def __str__(self):
                return self.bio




class Schedule(models.Model):
    day = models.CharField(max_length=150)
    time = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    posted_time = models.DateTimeField(auto_now=True) 
    

    def save_schedules(self):
        self.save()
    def delete_schedule(self):
        self.delete()    
    
    @classmethod
    def get_all_schedules(cls):
        schedules = Image.objects.all()
        return schedules 
    
    @classmethod
    def get_schedule_by_id(cls, id):
        schedule = cls.objects.filter(id=id).all()
        return schedule     
    @classmethod
    def display_schedules(cls):
        projects=cls.objects.all()
        return schedules                

