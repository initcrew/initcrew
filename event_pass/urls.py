from django.urls import path
from .views import *

urlpatterns = [
  path('', index, name='event_home'),
  path('meetup_pass/', meetup_pass, name='meetup_pass'),
  path('download/', download, name='download'),
  path('cancel/', cancel, name='cancel'),
  path('error/', error, name='error')
]