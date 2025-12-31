from .models import Note
from rest_framework import serializers

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields= ['id', 'title', 'content', 'created_at' ]
    
    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)