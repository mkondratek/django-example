from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from notes.models import Note


class NoteCreate(CreateView):
    model = Note
    fields = ['title', 'body']


class NoteUpdate(UpdateView):
    model = Note
    fields = ['title', 'body']
    template_name_suffix = '_update_form'


class NoteDelete(DeleteView):
    model = Note
    success_url = reverse_lazy('note-list')


class NoteListView(ListView):
    model = Note


class NoteDetailView(DetailView):
    model = Note
