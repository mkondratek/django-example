from django.urls import path

from notes.views import NoteListView, NoteDetailView, NoteCreate, NoteUpdate, NoteDelete

urlpatterns = [
    path('', NoteListView.as_view(), name='note-list'),
    path('<int:pk>/', NoteDetailView.as_view(), name='note-detail'),
    path('add/', NoteCreate.as_view(), name='note-add'),
    path('<int:pk>/update/', NoteUpdate.as_view(), name='note-update'),
    path('<int:pk>/delete/', NoteDelete.as_view(), name='note-delete'),
]
