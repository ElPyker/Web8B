from django.contrib import admin

# Register your models here.

from core import models

@admin.register(models.GrantGoal)
class GrantGoalAdmin(admin.ModelAdmin):
    list_display = ["ggname", "user", "timestamp", "final_date", "days_duration", "status"]
    
@admin.register(models.SubGrantGoal)
class SubGrantGoalAdmin(admin.ModelAdmin):
    list_display = ["sggname", "user", "timestamp", "final_date", "days_duration", "status"]
    
@admin.register(models.Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display = ["goalname", "user", "timestamp", "final_date", "days_duration", "status"]
    
@admin.register(models.Issue)
class IssueAdmin(admin.ModelAdmin):
    list_display = ["issuename", "user", "timestamp", "final_date", "days_duration", "status"]
    
@admin.register(models.Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ["area_name", "description"]