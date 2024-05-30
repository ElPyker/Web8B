from django.db import models
from django.contrib.auth.models import User
from core.models import Area
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=128, default="I Love Plesem System")
    avatar = models.ImageField(blank=True, null=True)
    timestamp = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    status = models.BooleanField(default=True)
    slug = models.SlugField(max_length=8, unique=True) 

    def __srt__(self):
        return self.user.first_name
    
@receiver(post_save, sender=User)
def auto_profile(sender, instance, **kwargs):
    if kwargs.get('created', False):
        Profile.objects.get_or_create(user=instance)