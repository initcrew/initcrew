from django.contrib import admin
from .models import Event, Team, Project

# Register your models here.
class EventAdmin(admin.ModelAdmin):
  list_display = ['title', 'is_upcoming', 'alignment', 'created_at']
  list_editable = ('is_upcoming', 'alignment',)
  list_filter = ('is_upcoming', 'alignment',)

class TeamAdmin(admin.ModelAdmin):
  list_display = ['name', 'position', 'is_admin', 'created_at']
  list_editable = ('is_admin',)
  list_filter = ('is_admin', 'position',)

class ProjectAdmin(admin.ModelAdmin):
  list_display = ['name', 'url', 'created_at']

admin.site.register(Event, EventAdmin)
admin.site.register(Team, TeamAdmin  )
admin.site.register(Project, ProjectAdmin)