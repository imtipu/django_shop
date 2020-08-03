from django.contrib import admin

from .models import *
# Register your models here.


class ProductTagsAdminInline(admin.TabularInline):
    model = ProductTags
    # filter_horizontal = ['tags']
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created', 'updated']
    filter_horizontal = ('tags', )
    inlines = [ProductTagsAdminInline]
    # list_editable = ['tags']


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ['id', 'tag']
