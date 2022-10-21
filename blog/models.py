from email.policy import default
from django.db import models

# Create your models here.
class BlogPost(models.Model):
  title = models.CharField(max_length=350, unique=True)
  post_slug = models.SlugField(max_length=350, unique=True)
  author = models.CharField(max_length=150)
  intro = models.TextField(blank=True)
  body = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  is_approved = models.BooleanField(default=False)

  def __str__(self):
    return self.title