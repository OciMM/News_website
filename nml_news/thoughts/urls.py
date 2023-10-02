from django.urls import path
from . import views

urlpatterns = [
    path('', views.ThoughtsView.as_view(), name='thoughts'),
    path('<slug:slug>/', views.ThoughtsDetailsView.as_view(), name='thoughts_details')
]
