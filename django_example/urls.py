"""django_example URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from notes.views import NoteDelete, NoteUpdate, NoteCreate

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'note/add/$', NoteCreate.as_view(), name='note-add'),
    url(r'note/(?P<pk>[0-9]+)/$', NoteUpdate.as_view(), name='note-update'),
    url(r'note/(?P<pk>[0-9]+)/delete/$', NoteDelete.as_view(), name='note-delete'),
]
