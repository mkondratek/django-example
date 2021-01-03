from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from notes.models import Note


class NoteCreate(CreateView):
    model = Note
    fields = ['title', 'body']


class NoteUpdate(UpdateView):
    model = Note
    fields = ['title', 'body']


class NoteDelete(DeleteView):
    model = Note
    success_url = reverse_lazy('note-list')
