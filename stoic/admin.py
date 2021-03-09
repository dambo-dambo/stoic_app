from django.contrib import admin

from .models import Stoic


class StoicAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'updated_at', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')

admin.site.register(Stoic, StoicAdmin)

