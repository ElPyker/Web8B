from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import timedelta

# Create your models here.

# Esta es una lista de opciones para que el usuario pueda seleccionar
CHOICES_LEVEL = (
    ("HIGH", "HG"),
    ("MIDDLE", "MD"),
    ("LOW", "LW")
)

CHOICES_STATE = {
    ("PENDING", "PD"),
    ("IN PROGRESS", "IP"),
    ("DONE", "DN")
}


class GrantGoal(models.Model):
    ggname = models.CharField(max_length=64, default="Generic Grant Goal")
    description = models.CharField(max_length=128, default="Generic Grant Goal description")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateField(auto_now_add=True, auto_now=False)
    days_duration = models.IntegerField(default=7)
    final_date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    progress = models.FloatField(default=0.0)
    priority = models.CharField(max_length=8, choices=CHOICES_LEVEL)
    state = models.CharField(max_length=16, choices=CHOICES_STATE)
    status = models.BooleanField(default=True)
    slug = models.SlugField(max_length=8)

    def __str__(self):
        return self.ggname
    
@receiver(post_save, sender=GrantGoal)
def auto_final_date_GG(sender, instance, **kwargs):
    if instance.final_date is None or instance.final_date=='':
        instance.final_date = instance.timestamp + timedelta(days=instance.days_duration)
        instance.save()




class Area(models.Model):
    area_name = models.CharField(max_length=32, default="Generic Area")
    description = models.CharField(max_length=128, default="Generic Activities")

    def __str__(self):
        return self.area_name



CHOICES_LEVEL_SUB = (
    ("HIGH", "HG"),
    ("MIDDLE", "MD"),
    ("LOW", "LW")
)

CHOICES_STATE_SUB = {
    ("PENDING", "PD"),
    ("IN PROGRESS", "IP"),
    ("DONE", "DN")
}


class SubGrantGoal(models.Model):
    sggname = models.CharField(max_length=64, default="Generic Sub Grant Goal")
    description = models.CharField(max_length=128, default="Generic Sub Grant Goal description")
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    grantgoal = models.ForeignKey(GrantGoal, on_delete = models.CASCADE)
    timestamp = models.DateField(auto_now_add=True, auto_now=False)
    days_duration = models.IntegerField(default=7)
    final_date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    progress = models.FloatField(default=0.0)
    priority = models.CharField(max_length=8, choices=CHOICES_LEVEL_SUB)
    state = models.CharField(max_length=16, choices=CHOICES_STATE_SUB)
    status = models.BooleanField(default=True)
    slug = models.SlugField(max_length=8)

    def __str__(self):
        return self.sggname


@receiver(post_save, sender=SubGrantGoal)
def auto_final_date_SGG(sender, instance, **kwargs):
    if instance.final_date is None or instance.final_date=='':
        instance.final_date = instance.timestamp + timedelta(days=instance.days_duration)
        instance.save()

    
    
CHOICES_LEVEL_GOAL = (
    ("HIGH", "HG"),
    ("MIDDLE", "MD"),
    ("LOW", "LW")
)

CHOICES_STATE_GOAL = {
    ("PENDING", "PD"),
    ("IN PROGRESS", "IP"),
    ("DONE", "DN")
}


class Goal(models.Model):
    goalname = models.CharField(max_length=64, default="Generic Goal")
    description = models.CharField(max_length=128, default="Generic Goal description")
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subgrantgoal = models.ForeignKey(SubGrantGoal, on_delete = models.CASCADE)
    timestamp = models.DateField(auto_now_add=True, auto_now=False)
    days_duration = models.IntegerField(default=7)
    final_date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    progress = models.FloatField(default=0.0)
    priority = models.CharField(max_length=8, choices=CHOICES_LEVEL_GOAL)
    state = models.CharField(max_length=16, choices=CHOICES_STATE_GOAL)
    status = models.BooleanField(default=True)
    slug = models.SlugField(max_length=8)

    def __str__(self):
        return self.goalname


@receiver(post_save, sender=Goal)
def auto_final_date_G(sender, instance, **kwargs):
    if instance.final_date is None or instance.final_date=='':
        instance.final_date = instance.timestamp + timedelta(days=instance.days_duration)
        instance.save()


    
CHOICES_LEVEL_ISSUE = (
    ("HIGH", "HG"),
    ("MIDDLE", "MD"),
    ("LOW", "LW")
)

CHOICES_STATE_ISSUE = {
    ("PENDING", "PD"),
    ("IN PROGRESS", "IP"),
    ("DONE", "DN")
}


class Issue(models.Model):
    issuename = models.CharField(max_length=64, default="Generic Issue")
    description = models.CharField(max_length=128, default="Generic Issue description")
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    goal = models.ForeignKey(Goal, on_delete = models.CASCADE)
    timestamp = models.DateField(auto_now_add=True, auto_now=False)
    days_duration = models.IntegerField(default=7)
    final_date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    progress = models.FloatField(default=0.0)
    priority = models.CharField(max_length=8, choices=CHOICES_LEVEL_ISSUE)
    state = models.CharField(max_length=16, choices=CHOICES_STATE_ISSUE)
    status = models.BooleanField(default=True)
    slug = models.SlugField(max_length=8)

    def __str__(self):
        return self.issuename



@receiver(post_save, sender=Issue)
def auto_final_date_I(sender, instance, **kwargs):
    if instance.final_date is None or instance.final_date=='':
        instance.final_date = instance.timestamp + timedelta(days=instance.days_duration)
        instance.save()