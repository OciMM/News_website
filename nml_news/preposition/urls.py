from django.urls import path
from . import views

urlpatterns = [
    path('', views.preposition_upload, name='preposition')
]
