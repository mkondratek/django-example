from django.db import models
from django.urls import reverse


class Note(models.Model):
    title = models.CharField(max_length=256)
    body = models.TextField()

    def get_absolute_url(self):
        return reverse('note-detail', kwargs={'pk': self.pk})
