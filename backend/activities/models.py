from django.db import models


# Create your models here.
class Activity(models.Model):

    class ActivityType(models.TextChoices):
        START = 'ST', 'Start'
        END = 'EN', 'End'
        NORMAL = 'NO', 'Normal'

    name = models.CharField('first name', max_length=30, default="")
    type = models.CharField(max_length=2, choices=ActivityType.choices, default=ActivityType.NORMAL)
    end_date = models.DateTimeField(auto_now_add=True)
    score = models.IntegerField(default=5)
