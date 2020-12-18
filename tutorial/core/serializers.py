from rest_framework import serializers
from core.models import Snippet

class SnippetSerializer(serializers.ModelSerializer):
    "Snipper serializers"

    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'language', 'created_at']
