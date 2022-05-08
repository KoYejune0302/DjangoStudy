from newbie_django_seminar.notes.models import User
from rest_framework import serializers
from notes.models import Note, User, Comment, Course


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','nickname', 'email']


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'created_by','title', 'content']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'created_by', 'parent_note', 'content']


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'class_id', 'title']


