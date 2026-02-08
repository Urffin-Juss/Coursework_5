from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
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

    @swagger_auto_schema(
        operation_description="Создание",
        operation_summary="habit_create",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "habit_name": openapi.Schema(
                    type=openapi.TYPE_STRING, description="Название привычки"
                ),
                "owner": openapi.Schema(
                    type=openapi.TYPE_INTEGER, description="Создатель привычки"
                ),
                "place": openapi.Schema(
                    type=openapi.TYPE_STRING, description="Место выполнения привычки"
                ),
                "time": openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description="Время для выполнения привычки. Не может превышать 120 секунд.",
                ),
                "action": openapi.Schema(
                    type=openapi.TYPE_STRING, description="Действие"
                ),
                "is_pleasant": openapi.Schema(
                    type=openapi.TYPE_BOOLEAN,
                    description="Признак полезной привычки. Не может указываться у привычек с выбранным reward и \
                        если выбрано related_habit",
                ),
                "related_habit": openapi.Schema(
                    type=openapi.TYPE_INTEGER,
                    description="Связанная привычка. Должна быть привычка с признаком is_pleasant. Не может быть \
                        указана у привычки с признаком is_pleasant и если выбрано reward",
                ),
                "periodicity": openapi.Schema(
                    type=openapi.TYPE_INTEGER,
                    description="Периодичность выполнения. Должна быть в диапазоне от 1 до 7 дней.",
                ),
                "reward": openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description="Вознаграждение. Не может быть указана у привычки с признаком is_pleasant и если \
                        выбрана related_habit",
                ),
                "time_to_complete": openapi.Schema(
                    type=openapi.TYPE_INTEGER,
                    description="Время на выполнение привычки",
                ),
                "is_public": openapi.Schema(
                    type=openapi.TYPE_BOOLEAN, description="Признак публичной привычки"
                ),
            },
            required=["habit_name", "place", "action", "time_to_complete"],
        ),
        responses={
            "201": openapi.Response(
                description="Объект создан",
                schema=HabitSerializer,
                examples={
                    "application/json": {
                        "id": 1,
                        "owner": 3,
                        "habit_name": "Отжимания",
                        "place": "В любом месте",
                        "time": "18:32:00",
                        "action": "Отжимания",
                        "is_pleasant": False,
                        "periodicity": 1,
                        "reward": None,
                        "is_public": False,
                        "time_to_complete": 120,
                        "created_at": "2026-02-07T18:14:38.910300+03:00",
                    }
                },
            ),
            "400": "Ошибки валидации",
            "401": "Не авторизован",
        },
        tags=["habit"],
    )


    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PublicHabitViewSet(viewsets.ModelViewSet, ReadOnlyModelViewSet):
    queryset = Habit.objects.filter(is_public=True)
    serializer_class = HabitsSerializer
    permission_classes = [AllowAny]
    pagination_class = HabitPagination