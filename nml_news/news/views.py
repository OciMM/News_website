from django.shortcuts import render
from django.views.generic.base import View

from . import models


class NewsView(View):
    """Получение страниц новостей"""
    def get(self, request):
        news = models.News.objects.all()
        return render(request, 'news/news.html', {'news_list': news})


class NewsDetailView(View):
    """Получение информации для страницы новостей"""
    def get(self, request, slug):
        news_details = models.News.objects.get(slug=slug)
        return render(request, 'news/news_details.html', {'news_details': news_details})

