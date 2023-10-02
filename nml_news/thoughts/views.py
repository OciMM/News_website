from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View
from django.views.generic import ListView, DetailView

from . import models


class ThoughtsView(View):
    """Запрос по обработке шаблона и передачи информации"""
    def get(self, reqeust):
        thoughts_list = models.Thoughts.objects.all()
        return render(reqeust, 'thoughts/thoughts.html', {'thoughts_list': thoughts_list})


class ThoughtsDetailsView(View):
    """Запрос на обработку детального шаблона и передачи точной детальной информации"""
    def get(self, request, slug):
        thoughts_list = get_object_or_404(models.Thoughts, slug=slug)
        return render(request, 'thoughts/thoughts_details.html', {'thoughts_list': thoughts_list})
