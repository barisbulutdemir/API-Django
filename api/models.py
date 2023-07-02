from django.db import models

class Note(models.Model):
    body = models.TextField(max_length=255, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    # admin panelinde direk notun ismini görmek için
    def __str__(self):
        return self.body[0:50]