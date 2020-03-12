from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('question/<int:pk>/', views.question, name='question'),
    path('check/<int:pk>/', views.check, name='check'),
]