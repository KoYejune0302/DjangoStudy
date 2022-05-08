from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from newbie_django_seminar.notes.models import Note
from rest_framework.parsers import JSONParser

from rest_framework import viewsets
from notes.models import Note, User, Comment, Course
from notes.serializers import NoteSerializer, UserSerializer, CommentSerializer, CourseSerializer

# @csrf_exempt
# def note_list(request):
#     if request.method == 'GET':
#         notes = Note.objects.all()
#         serializer = NoteSerializer(notes, many=True)
#         return JsonResponse(serializer.data, safe=False)
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = NoteSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)

# @csrf_exempt
# def note_detail(request, pk):
#     try:
#         note = Note.objects.get(pk=pk)
#     except Note.DoesNotExist:
#         return HttpResponce(status=404)
    
#     if request.method =='GET':
#         serializer = NoteSerialier(note)
#         return JsonResponse(serializer.data)
#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = NoteSerializer(note, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)
#     elif request.method =='DELETE':
#         note.delete()
#     return HttpResponse(status=204)

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def perform_create(self, serializer):
        title = serilaizer.validated_data['title'].upper()
        serializer.save(title=title)

        content = serializer.validated_data['content'].replace("comment", "")
        serializer.save(content=content)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer