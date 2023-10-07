from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic import ListView, DetailView

from . import models


class NewsView(ListView):
    """Получение страниц новостей"""
    model = models.News
    queryset = models.News.objects.filter(draft=False).order_by('-start_at')[:12]
    template_name = 'news/news.html'
    context_object_name = "news_list"


class NewsDetailView(DetailView):
    """Получение информации для страницы новостей"""
    model = models.News
    slug_field = 'slug'
    template_name = 'news/news_details.html'
    context_object_name = 'news_details'
