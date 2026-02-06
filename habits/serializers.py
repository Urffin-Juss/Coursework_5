from paginators import HabitPagination
from rest_framework import serializers, permissions

from habits.models import Habit


class HabitsSerializer(serializers.ModelSerializer):


    class Meta:
        model = Habit
        fields = '__all__'
        read_only_fields = ('user')

        def __init__(self):
            self.instance = None

        def validate(self, attrs):
            is_pleasant = attrs.get('is_pleasant', getattr(self.instance, 'is_pleasant', False))
            reward = attrs.get('reward', getattr(self.instance, 'reward', None))
            related_habits = attrs.get('related_habits', getattr(self.instance, 'related_habits', None))
            time_to_complete = attrs.get('time_to_complete', getattr(self.instance, 'time_to_complete', None))
            periodicity = attrs.get('periodicity', getattr(self.instance, 'periodicity', None))


            if reward and related_habits:
                raise serializers.ValidationError ("You cannot set both reward and related_habits")

            if time_to_complete is not None and periodicity > 120:
                raise serializers.ValidationError ("Time to complete must be less than 120 minutes")

            if not(1 <= periodicity <= 7):
                raise serializers.ValidationError ("Periodicity must be between 1 and 7")

            if is_pleasant and (reward or related_habits):
                raise serializers.ValidationError ("Pleasant and reward cannot be set at the same time")

            if related_habits and not related_habits.is_pleasant:
                raise serializers.ValidationError ("Related habits need to be a pleasant")





