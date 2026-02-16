from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.fields import DateTimeField
from rest_framework.test import APITestCase

from habits.models import Habit






class LessonTestCase(APITestCase):

    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(
            "testuser",
            "test@test.com",
            "12345"
        )
        self.habit = Habit.objects.create(
            owner=self.user,
            habit_name="Просмотр шортсов",
            place="Любое место",
            action="Просмотр шортсов",
            time_to_complete="120",
        )
        self.client.force_authenticate(user=self.user)

    def test_habit_retrieve(self):
        url = reverse("habits:habit-detail", args=(self.habit.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("habit_name"), self.habit.habit_name)

    def test_habit_create(self):
        url = reverse("habits:habit-list")
        data = {
            "habit_name": "Приседания",
            "place": "Любое место",
            "action": "Приседания",
            "time_to_complete": "100",
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.all().count(), 2)

    def test_habit_update(self):
        url = reverse("habits:habit-detail", args=(self.habit.pk,))
        data = {
            "habit_name": "Приседания",
            "place": "Любое место",
            "action": "Приседания",
            "time_to_complete": "50",
        }
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("time_to_complete"), 50)

    def test_habit_delete(self):
        url = reverse("habits:habit-detail", args=(self.habit.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habit.objects.all().count(), 0)

    def test_habits_list(self):
        url = reverse("habits:habit-list")
        response = self.client.get(url)
        data = response.json()
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.habit.pk,
                    "owner": self.user.pk,
                    "habit_name": "Просмотр шортсов",
                    "place": "Любое место",
                    "time": None,
                    "action": "Просмотр шортсов",
                    "is_pleasant": False,
                    "periodicity": 1,
                    "reward": None,
                    "is_public": False,
                    "time_to_complete": 120,
                    "created_at": DateTimeField().to_representation(
                        self.habit.created_at
                    ),
                }
            ],
        }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)