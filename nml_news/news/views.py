from django.shortcuts import render
from django.views.generic.base import View

from . import models


class IndexView(View):
    """Получение главной страницы"""
    def get(self, request):
        return render(request, 'news/index.html')


class NewsView(View):
    """Получение страниц новостей"""
    def get(self, request):
        news = models.News.objects.all()
        return render(request, 'news/news.html', {'news_list': news})


class NewsDetailView(View):
    """Получение информации для страницы новостей"""
    def get(self, request, pk):
        newses = models.News.objects.get(id=pk)
        return render(request, 'news/single.html', {'newses': newses})

