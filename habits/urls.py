from django.urls import path, include

from habits.views import HabitsViewSet

app_name = 'habits'

urlpatterns = [
    path('', HabitsViewSet.as_view(), name='habits'),


]