from django.contrib import admin
from .models import MeetupPass

# Register your models here.
class MeetupPassAdmin(admin.ModelAdmin):
  list_display = ['name', 'email', 'code', 'count', 'is_coming']
  list_filter = ('is_coming',)

admin.site.register(MeetupPass, MeetupPassAdmin)