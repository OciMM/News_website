from django.shortcuts import render
from django.views.generic.base import View


class IndexView(View):
    """Получение главной страницы"""
    def get(self, request):
        return render(request, 'index/index.html')
