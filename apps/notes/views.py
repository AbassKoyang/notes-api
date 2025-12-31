from django.shortcuts import render

from .models import Note
from .serializers import NoteSerializer
from .permissions import IsOwner

from rest_framework import generics, filters, permissions
# Create your views here.


class ListCreateNoteView(generics.ListCreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']
    queryset = Note.objects.all()


    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset()
        request = self.request
        user = request.user
        if not user.is_authenticated:
            return Note.objects.none()
        return qs.filter(user=user)

class UpdateNoteView(generics.UpdateAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsOwner]
    queryset = Note.objects.all()
    lookup_field = 'pk'
    
    def perform_update(self, serializer):
        instance = serializer.save();
        if not instance.content:
            instance.content = instance.title
            instance.save()


class RetrieveNoteView(generics.RetrieveAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsOwner]
    queryset = Note.objects.all()
    lookup_field = 'pk'


class DeleteNoteView(generics.DestroyAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsOwner]
    queryset = Note.objects.all()
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()