from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework import generics
from rest_framework import permissions
from .serializers import TutorSerializer, CategorySerializer, CourseSerializer, ChapterSerializer,LearnerSerializer
from . import models
class TutorList(generics.ListCreateAPIView):
   queryset = models.Tutor.objects.all()
   serializer_class = TutorSerializer
  # permission_classes = [permissions.IsAuthenticated]

class TutorDetail(generics.RetrieveUpdateDestroyAPIView):
   queryset = models.Tutor.objects.all()
   serializer_class = TutorSerializer
   #permission_classes = [permissions.IsAuthenticated]
@csrf_exempt
def tutor_login(request):
   email = request.POST['email']
   passsword = request.POST['password']
   tutorData = models.Tutor.objects.get(email=email,password=passsword)
   if tutorData:
      return JsonResponse({'bool':True, 'tutor_id': tutorData.id})
   else:
      return JsonResponse({'bool':False})

#CourseCategory
class CategoryList(generics.ListCreateAPIView):
   queryset = models.CourseCategory.objects.all()
   serializer_class = CategorySerializer

#Course
class CourseList(generics.ListCreateAPIView):
   queryset = models.Course.objects.all()
   serializer_class = CourseSerializer

#SpecificTutorCourse
class TutorCourseList(generics.ListCreateAPIView):
   serializer_class = CourseSerializer

   def get_queryset(self):
      tutor_id = self.kwargs['tutor_id']
      tutor = models.Tutor.objects.get(pk=tutor_id)
      return models.Course.objects.filter(tutor=tutor)

#Chapter
class ChapterList(generics.ListCreateAPIView):
   queryset = models.Chapter.objects.all()
   serializer_class = ChapterSerializer

# Learner Data
class LearnerList(generics.ListCreateAPIView):
   queryset = models.Learner.objects.all()
   serializer_class = LearnerSerializer
  # permission_classes = [permissions.IsAuthenticated]