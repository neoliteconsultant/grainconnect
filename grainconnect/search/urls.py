from django.urls import path

from . import views

urlpatterns = [
    path('search_array', views.get_index, name='search_array'),
]