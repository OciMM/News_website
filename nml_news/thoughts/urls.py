from django.urls import path
from . import views

urlpatterns = [
    path('', views.ThoughtsView.as_view(), name='thoughts'),
    path('post', views.thoughts_detail, name='thoughts_details')
]
