from django.shortcuts import render
from django.http import HttpResponse


def show(request):
    return HttpResponse("Hello from Notes app.")


def show_html(request):
    data = {
        'title': 'My Notes',
        'notes': ["Note 1", "Note 2", "Note 3"]
    }
    return render(request, 'notes/notes.html', data)