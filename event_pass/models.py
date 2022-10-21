from django.db import models

# Create your models here.
class MeetupPass(models.Model):
  name = models.CharField(max_length=150)
  email = models.EmailField()
  code = models.CharField(max_length=10, unique=True)
  count = models.IntegerField(default=0)
  is_coming = models.BooleanField(default=True)
  pass_image = models.ImageField(upload_to='photos/meetup_pass', blank=True)

  def __str__(self):
    return self.name