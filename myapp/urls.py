from django import urls
from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search_by_name, name='search_by_name'),

]
