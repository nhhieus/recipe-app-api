from django.db import models

LANGUAGES_CHOICES = []

class Snippet(models.Model):
    "Snippet model class"

    id = models.AutoField(primary_key=True),
    title = models.CharField(max_length=255),
    code = models.TextField(), 
    language = models.CharField(max_length=25),
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']


