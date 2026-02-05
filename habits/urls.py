from django.urls import path, include
from rest_framework.routers import DefaultRouter

from habits.views import HabitsViewSet

app_name = 'habits'
router = DefaultRouter()
router.register(r'habits', HabitsViewSet, basename='habits')

urlpatterns = [



]+router.urls