from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *


def show(request):
    return HttpResponse("Hello from Notes app.")


def show_html(request):
    notes = Note.objects.all()
    return render(request, 'notes/notes.html', {'notes': notes})


def add_note(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('notes')
    else:
        form = AddPostForm()
    return render(request, 'notes/add_note.html', {'form': form, 'title': 'Add note'})


def edit_note(request, note_id):
    note = Note.objects.get(id=note_id)

    if request.method == 'POST':
        form = EditNoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('notes')
    else:
        form = EditNoteForm(instance=note)

    return render(request, 'notes/edit_note.html', {'form': form, 'note': note, 'title': 'Edit note'})


def delete_note(request, note_id):
    note = Note.objects.get(id=note_id)
    note.delete()
    return redirect('notes')

