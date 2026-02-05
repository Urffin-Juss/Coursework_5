from rest_framework import viewsets, permissions

from habits.models import Habit
from habits.serializers import RelatedHabitsSerializer, HabitsSerializer


class HabitsViewSet(viewsets.ModelViewSet):
    queryset = Habit.objects.all()
    model = Habit
    serializer_class = HabitsSerializer
    permission_classes = [permissions.AllowAny]


