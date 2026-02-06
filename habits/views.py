from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import Habit
from .serializers import HabitsSerializer
from .permissions import IsOwner
from .paginators import HabitPagination


class HabitViewSet(viewsets.ModelViewSet):
    serializer_class = HabitsSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    pagination_class = HabitPagination

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PublicHabitViewSet(viewsets.ModelViewSet, ReadOnlyModelViewSet):
    queryset = Habit.objects.filter(is_public=True)
    serializer_class = HabitsSerializer
    permission_classes = [AllowAny]
    pagination_class = HabitPagination