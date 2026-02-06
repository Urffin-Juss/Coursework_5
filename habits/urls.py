from django.urls import path, include
from rest_framework.routers import DefaultRouter


from habits.views import HabitViewSet, PublicHabitViewSet

app_name = 'habits'
router = DefaultRouter()
router.register(r'habits', HabitViewSet, basename='habits')
router.register(r'public-habits', PublicHabitViewSet, basename='public-habits')

urlpatterns = router.urls