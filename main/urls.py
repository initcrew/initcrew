from django.urls import path
from .views import *

urlpatterns = [
  path('', home, name='home'),
  path('team/', team, name='team'),
  path('contact/', contact, name='contact'),
  path('projects', projects, name='projects')
]