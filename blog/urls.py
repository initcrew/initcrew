from django.urls import path
from .views import *

urlpatterns = [
  path('', blog_home, name='blog_home'),
  path('<slug:post_slug>', blog_post, name='blog_post'),
  path('add/', add_blog, name='add_blog')
]