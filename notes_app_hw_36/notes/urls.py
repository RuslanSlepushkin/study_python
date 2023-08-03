from django.urls import path
from . import views

urlpatterns = [
    path('', views.show, name='show'),
    path('notes', views.show_html, name='show_html'),
]