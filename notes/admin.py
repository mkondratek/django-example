from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin

from notes.models import Note, Topic

admin.site.register(Note)


@admin.register(Topic)
class TopicAdmin(DjangoMpttAdmin):
    pass
