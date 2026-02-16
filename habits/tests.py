from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habit


class LessonTestCase(APITestCase):
    def setUp(self):
        User = get_user_model()

        # create_user у стандартного User ожидает username, email, password
        self.user = User.objects.create_user(
            username="testuser",
            email="test@test.com",
            password="12345",
        )

        self.habit = Habit.objects.create(
            user=self.user,
            action="Просмотр шортсов",
            place="Любое место",
            time="12:00:00",
            is_pleasant=False,
            periodicity=1,
            reward=None,
            time_to_complete=120,
            is_public=False,
            related_habit=None,
        )

        self.client.force_authenticate(user=self.user)

    def test_habit_retrieve(self):
        url = reverse("habits:habits-detail", args=(self.habit.pk,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = response.json()
        self.assertEqual(data["id"], self.habit.pk)
        self.assertEqual(data["action"], self.habit.action)
        self.assertEqual(data["place"], self.habit.place)
        self.assertEqual(data["time_to_complete"], self.habit.time_to_complete)

    def test_habit_create(self):
        url = reverse("habits:habits-list")
        payload = {
            "action": "Приседания",
            "place": "Любое место",
            "time": "12:00:00",
            "time_to_complete": 100,
            # остальное пусть проставится дефолтами модели/сериализатора
        }

        response = self.client.post(url, payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.count(), 2)

        created = response.json()
        self.assertEqual(created["action"], payload["action"])
        self.assertEqual(created["place"], payload["place"])
        self.assertEqual(created["time_to_complete"], payload["time_to_complete"])

    def test_habit_update(self):
        url = reverse("habits:habits-detail", args=(self.habit.pk,))
        payload = {
            "time_to_complete": 50,
            "action": "Приседания",
        }

        response = self.client.patch(url, payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = response.json()
        self.assertEqual(data["time_to_complete"], 50)
        self.assertEqual(data["action"], "Приседания")

        self.habit.refresh_from_db()
        self.assertEqual(self.habit.time_to_complete, 50)
        self.assertEqual(self.habit.action, "Приседания")

    def test_habit_delete(self):
        url = reverse("habits:habits-detail", args=(self.habit.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habit.objects.count(), 0)

    def test_habits_list(self):
        url = reverse("habits:habits-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = response.json()

        # Если включена пагинация DRF:
        if isinstance(data, dict) and "results" in data:
            results = data["results"]
        else:
            # Если пагинации нет и возвращается список
            results = data

        self.assertEqual(len(results), 1)
        item = results[0]
        self.assertEqual(item["id"], self.habit.pk)
        self.assertEqual(item["action"], self.habit.action)
        self.assertEqual(item["place"], self.habit.place)
        self.assertEqual(item["time_to_complete"], self.habit.time_to_complete)