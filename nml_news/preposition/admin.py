from django.contrib import admin
from . import models


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(models.PrepositionModel)
class PrepositionModelAdmin(admin.ModelAdmin):
    list_display = ('category', 'date')
    list_filter = ('category', 'date')
