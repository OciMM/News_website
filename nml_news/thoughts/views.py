from django.shortcuts import render
from django.views.generic.base import View


class ThoughtsView(View):
    def get(self, request):
        return render(request, 'thoughts/thoughts.html')
