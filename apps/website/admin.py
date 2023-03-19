from django.contrib import admin
from .models import *


class WebSiteInline(admin.TabularInline):
    model = WebSite
    extra = 0
    fields = ['name', 'url']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name', 'description']
    readonly_fields = ['created_time', 'updated_time']
    inlines = [WebSiteInline]
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
    search_fields = ['name']
    list_display = ['name', 'category', 'url']
    list_filter = ['category']
    readonly_fields = ['created_time', 'updated_time']
    autocomplete_fields = ['category']
    fieldsets = (
        (None, {
            'fields': ('name', 'category', 'url', 'description'),
        }),
        ('其他链接', {
            'classes': ('collapse',),
            'fields': ('extra_urls',),
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
