from django.shortcuts import render
from django.http import HttpResponse
from .models import Note

def show(request):
    return HttpResponse("Hello from Notes app.")


def show_html(request):
    notes = Note.objects.all()
    return render(request, 'notes/notes.html', {'notes': notes})