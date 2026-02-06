from django.urls import path, include
from rest_framework.routers import DefaultRouter

from habits.views import HabitsViewSet, PublicHabitViewSet

app_name = 'habits'
router = DefaultRouter()
router.register(r'habits', HabitsViewSet, basename='habits')
router.register(r'public-habits', PublicHabitViewSet, basename='public-habits')

urlpatterns = router.urls