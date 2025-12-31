from rest_framework import generics
from rest_framework import permissions 
from django.conf import settings
from .serializers import RegisterSerializer
from django.contrib.auth.models import User

# Create your views here.
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]