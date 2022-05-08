from django.db import models


class User(models.Model):
    nickname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    
# Create your models here.
class Note(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=None, blank=True)

    class Meta:
        ordering = ['created']

class Comment(models.Model):
    content = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment')
    parent_note = models.ForeignKey(Note, on_delete=models.CASCADE, related_name='comment', default=None, blank=True)

class Course(models.Model):
    class_id = models.TextField(max_length=100)
    title = models.TextField(max_length=100)