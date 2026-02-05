from rest_framework import viewsets, permissions

from habits.models import Habit
from habits.serializers import RelatedHabitsSerializer


class HabitsViewSet(viewsets.ModelViewSet):
    queryset = Habit.objects.all()
    model = Habit
    serializer_class = RelatedHabitsSerializer
    permission_classes = [permissions.AllowAny]


