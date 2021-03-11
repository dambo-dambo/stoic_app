from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Stoic, Month


class StoicAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'month', 'created_at', 'updated_at', 'is_published', 'get_photo')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'month')
    fields = ('title', 'month', 'content', 'photo', 'get_photo', 'is_published', 'views', 'created_at', 'updated_at')
    readonly_fields = ('get_photo', 'views', 'created_at', 'updated_at')
    save_on_top = True

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="75">')
        else:
            return '-'

    get_photo.short_description = 'Миниатюра'


class MonthAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


admin.site.register(Stoic, StoicAdmin)
admin.site.register(Month, MonthAdmin)

admin.site.site_title = 'Управление записями'
admin.site.site_header = 'Управление записями'