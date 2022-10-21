from django.contrib import admin
from .models import BlogPost

# Register your models here.
class BlogPostAdmin(admin.ModelAdmin):
  list_display = ['title', 'author']
  prepopulated_fields = {'post_slug': ('title',)}

admin.site.register(BlogPost, BlogPostAdmin)