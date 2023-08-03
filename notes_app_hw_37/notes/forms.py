from django import forms
from .models import *

class AddPostForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = '__all__'


class EditNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = '__all__'

