from django.contrib import admin
from . import models
from django import forms

from ckeditor_uploader.widgets import CKEditorUploadingWidget


class ThoughtsAdminForm(forms.ModelForm):
    """Model of the Ckeditor panel"""
    text = forms.CharField(label="Содержание", widget=CKEditorUploadingWidget())

    class Meta:
        model = models.Thoughts
        fields = '__all__'


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    """Admin panel of categories"""
    list_display = ('name', 'slug')
    search_fields = ('name',)


@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    """Admin panel of tags"""
    list_display = ('name', 'slug')
    search_fields = ('name',)


@admin.register(models.Thoughts)
class NewsAdmin(admin.ModelAdmin):
    """Admin panel of news"""
    list_display = ('id', 'title', 'category', 'start_at', 'update_at', 'draft')
    list_filter = ('id', 'category', 'start_at', 'update_at', 'draft')
    search_fields = ('id', 'title', 'category')
    form = ThoughtsAdminForm
