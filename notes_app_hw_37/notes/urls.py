from django.urls import path
from . import views

urlpatterns = [
    path('', views.show, name=''),
    path('notes', views.show_html, name='notes'),
    path('add_note', views.add_note, name='add_note'),
    path('note/<int:note_id>/edit', views.edit_note, name='edit_note'),
    path('note/<int:note_id>/delete', views.delete_note, name='delete_note'),
]
