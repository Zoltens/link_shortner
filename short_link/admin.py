from django.contrib import admin

from .models import Urls


@admin.register(Urls)
class UrlsAdmin(admin.ModelAdmin):
    list_display = ['user', 'httpurl']
    list_filter = ['user']
