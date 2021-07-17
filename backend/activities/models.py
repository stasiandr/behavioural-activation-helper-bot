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


class Session(models.Model):

    @property
    def is_active(self):
        return self.activities.filter(type=Activity.ActivityType.END).count() == 0

    def start_activity(self):
        act = Activity(type=Activity.ActivityType.START)
        act.save()
        self.activities.add(act)
        return act

    def add_activity(self, activity):
        self.activities.add(activity)
        return activity

    def end_activity(self):
        act = Activity(type=Activity.ActivityType.END)
        act.save()
        self.activities.add(act)
        return act

    activities = models.ManyToManyField(Activity, blank=True)
