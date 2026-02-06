from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models


class Habit(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="habits",
    )

    action = models.CharField(max_length=255)
    place = models.CharField(max_length=255)
    time = models.TimeField(str)

    is_pleasant = models.BooleanField(default=False)
    periodicity = models.PositiveSmallIntegerField(default=1)

    reward = models.CharField(max_length=255, null=True, blank=True)
    time_to_complete = models.PositiveSmallIntegerField()

    is_public = models.BooleanField(default=False)

    related_habit = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="linked_as_related",
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def clean(self):

        if self.reward and self.related_habit:
            raise ValidationError("Нельзя одновременно указывать reward и related_habit.")


        if self.time_to_complete > 120:
            raise ValidationError("time_to_complete должен быть не больше 120 секунд.")


        if not (1 <= self.periodicity <= 7):
            raise ValidationError("periodicity должна быть в диапазоне 1..7 дней.")


        if self.is_pleasant and (self.reward or self.related_habit):
            raise ValidationError("У приятной привычки не может быть reward или related_habit.")


        if self.related_habit and not self.related_habit.is_pleasant:
            raise ValidationError("related_habit должна быть приятной привычкой.")