from django.db import models
from django.conf import settings
from django.db import models



class Habit(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(unique=True, max_length=50)
    description = models.TextField(unique=True, null=False, blank=False,max_length=500)
    place = models.CharField(unique=True, max_length=50)
    time = models.TimeField(auto_now_add=True)
    is_pleasant = models.BooleanField(default=False)
    periodicity = models.PositiveIntegerField(default=1)
    related_habits = models.ManyToManyField('self',  related_name='related_habits')
    reward = models.IntegerField(default=0)
    time_to_complete = models.IntegerField(default=0, null=True, blank=True, verbose_name='Time To Complete')
    is_public = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-time']
        verbose_name = 'Habit'
        verbose_name_plural = 'Habits'

class RelatedHabits(Habit, models.Model):
    habit = models.ManyToManyField(Habit)
    habit_id = models.ForeignKey(Habit, on_delete=models.CASCADE)

    def __str__(self):
        return self.habit_id.title


