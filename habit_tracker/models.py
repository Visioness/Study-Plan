from django.db import models
from django.utils import timezone

# Create your models here.
class Habit(models.Model):
    name = models.CharField(max_length=40, default="Unnamed Habit")
    date = models.DateField(default=timezone.now)
    duration = models.IntegerField()