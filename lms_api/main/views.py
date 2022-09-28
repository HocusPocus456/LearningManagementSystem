from urllib import request
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
   try:
      tutorData = models.Tutor.objects.get(email=email,password=passsword)
   except models.Tutor.DoesNotExist:
      tutorData=None
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

   def get_queryset(self):
      qs=super().get_queryset()
      if 'result' in self.request.GET:
         limit=int(self.request.GET['result'])
         qs=models.Course.objects.all().order_by('-id')[:limit]
         return qs

#Course Detail
class CourseDetailView(generics.RetrieveAPIView):
   queryset=models.Course.objects.all()
   serializer_class=CourseSerializer

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
<<<<<<< HEAD
=======

>>>>>>> aafd83e2576d0e78806d96cf8aa2bc884f0e17ce
#Chapter
class CourseChapterList(generics.ListAPIView):
   serializer_class = ChapterSerializer

   def get_queryset(self):
      course_id = self.kwargs['course_id']
      course = models.Course.objects.get(pk=course_id)
      return models.Chapter.objects.filter(course=course)
<<<<<<< HEAD
 

@csrf_exempt
def learner_login(request):
   email = request.POST['email']
   passsword = request.POST['password']
   try:
      learnerData = models.Learner.objects.get(email=email,password=passsword)
   except models.Learner.DoesNotExist:
      learnerData=None
   if learnerData:
      return JsonResponse({'bool':True, 'learner_id': learnerData.id})
   else:
      return JsonResponse({'bool':False})
=======

#Chapter Detail
class ChapterDetailView(generics.RetrieveUpdateDestroyAPIView):
   queryset=models.Chapter.objects.all()
   serializer_class=ChapterSerializer
>>>>>>> aafd83e2576d0e78806d96cf8aa2bc884f0e17ce
