from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Note

# Create your tests here.

class NoteAPITestCase(APITestCase):

    def setUp(self):
        self.user1 = User.objects.create_user(
            username="user1",
            password="pass123"
        )
        self.user2 = User.objects.create_user(
            username="user2",
            password="pass123"
        )
    
    def test_user_can_create_note(self):
        self.client.force_authenticate(user=self.user1)

        data = {
            "title": "Test Note",
            "content": "Hello world"
        }

        response = self.client.post('/notes/', data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Note.objects.count(), 1)
        self.assertEqual(Note.objects.first().user, self.user1)

    def test_user_sees_only_their_notes(self):
        Note.objects.create(title="A", user=self.user1)
        Note.objects.create(title="B", user=self.user2)

        self.client.force_authenticate(user=self.user1)
        response = self.client.get("/notes/")
        print(response.data)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['title'], 'A')