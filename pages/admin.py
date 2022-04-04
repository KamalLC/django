from django.contrib import admin
from .models import HomePage, Blog
# Register your models here.

class HomePageAdmin(admin.ModelAdmin):
    list_display = ['id','title']

admin.site.register(HomePage,HomePageAdmin)
#admin.site.register(Blog)


class BlogAdmin(admin.ModelAdmin):
    list_display = ['id','title','created_at']
    list_filter = ['created_at']
    search_fields = ['title']

admin.site.register(Blog, BlogAdmin)