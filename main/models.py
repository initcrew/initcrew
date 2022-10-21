from email.policy import default
from django.db import models

# Create your models here.
class Event(models.Model):

  ALIGNMET = (
    ('Left', 'Left'),
    ('Right', 'Right')
  )

  title = models.CharField(max_length=250)
  description = models.TextField()
  image = models.ImageField(upload_to='photos/events')
  is_upcoming = models.BooleanField(default=True)
  alignment = models.CharField(max_length=10, choices=ALIGNMET, default='Left')
  link_1_title = models.CharField(max_length=100, blank=True, null=True)
  link_1_url = models.CharField(max_length=100, blank=True, null=True)
  link_2_title = models.CharField(max_length=100, blank=True, null=True)
  link_2_url = models.CharField(max_length=100, blank=True, null=True)
  link_3_title = models.CharField(max_length=100, blank=True, null=True)
  link_3_url = models.CharField(max_length=100, blank=True, null=True)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.title


class Team(models.Model):

  ROLES = (
    ('Founder', 'Founder'),
    ('Co-Founder', 'Co-Founder'),
    ('Core Team', 'Core Team')
  )

  name = models.CharField(max_length=200)
  position = models.CharField(max_length=30, choices=ROLES, default='Core Team')
  email = models.EmailField(blank=True, null=True)
  linkedin = models.CharField(max_length=300, blank=True, null=True)
  twitter = models.CharField(max_length=100, blank=True, null=True)
  is_admin = models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now_add=True)


class Project(models.Model):
  name = models.CharField(max_length=150)
  description = models.TextField()
  url = models.CharField(max_length=250, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.name