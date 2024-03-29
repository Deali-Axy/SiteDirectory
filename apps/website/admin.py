from django.contrib import admin
from .models import *


class WebSiteInline(admin.TabularInline):
    model = WebSite
    extra = 0
    fields = ['name', 'rank', 'url']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    sortable_by = ['rank', 'created_time', 'updated_time']
    search_fields = ['name']
    list_display = ['name', 'rank', 'created_time', 'updated_time']
    readonly_fields = ['created_time', 'updated_time']
    inlines = [WebSiteInline]
    fieldsets = (
        (None, {
            'fields': ('name', 'rank', 'description'),
        }),
        ('reserve fields', {
            'description': 'DjangoStarter 框架的保留字段',
            'classes': ('collapse',),
            'fields': (('created_time', 'updated_time'), 'is_deleted')
        })
    )


@admin.register(WebSite)
class WebSiteAdmin(admin.ModelAdmin):
    sortable_by = ['rank', 'created_time']
    search_fields = ['name']
    list_display = ['name', 'category', 'rank', 'url', 'created_time']
    list_filter = ['category']
    readonly_fields = ['created_time', 'updated_time']
    autocomplete_fields = ['category']
    fieldsets = (
        (None, {
            'fields': ('name', 'rank', 'category', 'url', 'description'),
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
