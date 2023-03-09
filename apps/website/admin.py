from django.contrib import admin
from .models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    readonly_fields = ['created_time', 'updated_time']
    fieldsets = (
        (None, {
            'fields': ('name', 'description'),
        }),
        ('reserve fields', {
            'description': 'DjangoStarter 框架的保留字段',
            'classes': ('collapse',),
            'fields': (('created_time', 'updated_time'), 'is_deleted')
        })
    )


@admin.register(WebSite)
class WebSiteAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'url']
    readonly_fields = ['created_time', 'updated_time']
    fieldsets = (
        (None, {
            'fields': ('name', 'category', 'description', 'url', 'extra_urls'),
        }),
        ('reserve fields', {
            'description': 'DjangoStarter 框架的保留字段',
            'classes': ('collapse',),
            'fields': (('created_time', 'updated_time'), 'is_deleted')
        })
    )


@admin.register(URL)
class URLAdmin(admin.ModelAdmin):
    list_display = ['url']


@admin.register(ClickLog)
class ClickLogAdmin(admin.ModelAdmin):
    list_display = ['created_time', 'website']
