from django.shortcuts import render
from django.views.generic.base import View

# импортирование из моделей других приложений
from news.models import News
from thoughts.models import Thoughts


class IndexView(View):
    """Получение главной страницы"""
    def get(self, request):
        news_list = News.objects.all()
        thoughts_list = Thoughts.objects.all()
        return render(request, 'index/index.html', {'news_list': news_list,
                                                    'thoughts_list': thoughts_list})

