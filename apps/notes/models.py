from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class NoteQuerySet(models.QuerySet):
    def active(self):
        return self.filter(is_deleted=False)

class NoteManager(models.Manager):
    def get_queryset(self):
        return NoteQuerySet(self.model, using=self._db)

    def active(self):
        return self.get_queryset().active()
        
class Note(models.Model):
    user = models.ForeignKey(User,
    on_delete=models.CASCADE,
    related_name='notes'
    )
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title
