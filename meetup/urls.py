from django.urls import path
from .views import *

urlpatterns = [
  path('team', meetup_team, name='meetup_team'),
]