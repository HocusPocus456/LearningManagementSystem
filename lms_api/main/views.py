from urllib import response
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework import generics
from rest_framework import permissions
from .serializers import CourseRatingSerializer, LearnerFavouriteCourseSerializer, TutorSerializer, TutorDashboardSerializer, CategorySerializer, CourseSerializer, ChapterSerializer,LearnerSerializer, LearnerCourseEnrollSerializer
from . import models
class TutorList(generics.ListCreateAPIView):
   queryset = models.Tutor.objects.all()
   serializer_class = TutorSerializer
  # permission_classes = [permissions.IsAuthenticated]

class TutorDetail(generics.RetrieveUpdateDestroyAPIView):
   queryset = models.Tutor.objects.all()
   serializer_class = TutorSerializer
   #permission_classes = [permissions.IsAuthenticated]

class TutorDashboard(generics.RetrieveAPIView):
   queryset=models.Tutor.objects.all()
   serializer_class=TutorDashboardSerializer
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
      qs = super().get_queryset()
      if 'result' in self.request.GET:
         limit = int(self.request.GET['result'])
         qs = models.Course.objects.all().order_by('-id')[:limit]

      if 'category' in self.request.GET:
         category = self.request.GET['category']
         qs = models.Course.objects.filter(techs__icontains=category)

      if 'skill_name' in self.request.GET and 'tutor' in self.request.GET:
         skill_name = self.request.GET['skill_name']
         tutor = self.request.GET['tutor']
         tutor = models.Tutor.objects.filter(id=tutor).first()
         qs = models.Course.objects.filter(techs__icontains=skill_name, tutor=tutor)

      elif 'learnerId' in self.kwargs:
         learner_id = self.kwargs['learnerId']
         learner = models.Learner.objects.get(pk=learner_id)
         print(learner.interested_subjects)
         queries = [Q(techs__iendswith=value) for value in learner.interested_subjects]
         query = queries.pop()
         for item in queries:
            query |= item
         qs = models.Course.objects.filter(query)
         return qs 
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

      #SpecificTutorCourse
class TutorCourseDetail(generics.RetrieveUpdateDestroyAPIView):
   queryset=models.Course.objects.all()
   serializer_class = CourseSerializer

'''
#Chapter
class ChapterList(generics.ListCreateAPIView):
   queryset = models.Chapter.objects.all()
   serializer_class = ChapterSerializer
'''
# Learner Data
class LearnerList(generics.ListCreateAPIView):
   queryset = models.Learner.objects.all()
   serializer_class = LearnerSerializer
  # permission_classes = [permissions.IsAuthenticated]


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

#Chapter
class CourseChapterList(generics.ListAPIView):
   serializer_class = ChapterSerializer

   def get_queryset(self):
      course_id = self.kwargs['course_id']
      course = models.Course.objects.get(pk=course_id)
      return models.Chapter.objects.filter(course=course)
 
#Chapter Detail
class ChapterDetailView(generics.RetrieveUpdateDestroyAPIView):
   queryset=models.Chapter.objects.all()
   serializer_class=ChapterSerializer

   def get_serializer_context(self):
      context = super().get_serializer_context()
      context['chapter_duration'] = self.chapter_duration
      print('context---------------------')
      print(context)
      return context

class LearnerEnrollCourseList(generics.ListCreateAPIView):
   queryset=models.LearnerCourseEnrollment.objects.all()
   serializer_class=LearnerCourseEnrollSerializer

class LearnerFavouriteCourseList(generics.ListCreateAPIView):
   queryset=models.LearnerFavouriteCourse.objects.all()
   serializer_class=LearnerFavouriteCourseSerializer

   def get_queryset(self):
      if 'learner_id' in self.kwargs:
         learner_id = self.kwargs['learner_id']
         learner = models.Learner.objects.get(pk=learner_id)
         return models.LearnerFavouriteCourse.objects.filter(learner=learner).distinct()


def fetch_enroll_status(request, learner_id, course_id):
   learner = models.Learner.objects.filter(id=learner_id).first()
   course= models.Course.objects.filter(id=course_id).first()
   enrollStatus=models.LearnerCourseEnrollment.objects.filter(course=course,learner=learner).count()
   if enrollStatus:
      return JsonResponse({'bool':True})
   else:
      return JsonResponse({'bool':False})

def fetch_favourite_status(request, learner_id, course_id):
   learner = models.Learner.objects.filter(id=learner_id).first()
   course= models.Course.objects.filter(id=course_id).first()
   favouriteStatus=models.LearnerFavouriteCourse.objects.filter(course=course,learner=learner).first()
   if favouriteStatus:
      return JsonResponse({'bool':True})
   else:
      return JsonResponse({'bool':False})

def remove_favourite_course(request, learner_id, course_id):
   learner = models.Learner.objects.filter(id=learner_id).first()
   course= models.Course.objects.filter(id=course_id).first()
   favouriteStatus=models.LearnerFavouriteCourse.objects.filter(course=course,learner=learner).delete()
   if favouriteStatus:
      return JsonResponse({'bool':True})
   else:
      return JsonResponse({'bool':False})

class EnrolledLearnerList(generics.ListAPIView):
   queryset=models.LearnerCourseEnrollment.objects.all()
   serializer_class=LearnerCourseEnrollSerializer

   def get_queryset(self):
      if 'course_id' in self.kwargs:
         course_id = self.kwargs['course_id']
         course = models.Course.objects.get(pk=course_id)
         return models.LearnerCourseEnrollment.objects.filter(course=course)
      elif 'tutor_id' in self.kwargs:
         tutor_id = self.kwargs['tutor_id']
         tutor = models.Tutor.objects.get(pk=tutor_id)
         return models.LearnerCourseEnrollment.objects.filter(course__tutor=tutor).distinct()
      elif 'learner_id' in self.kwargs:
         learner_id = self.kwargs['learner_id']
         learner = models.Learner.objects.get(pk=learner_id)
         return models.LearnerCourseEnrollment.objects.filter(learner=learner).distinct()

class LearnerEnrollCourseList(generics.ListCreateAPIView):
   queryset=models.LearnerCourseEnrollment.objects.all()
   serializer_class=LearnerCourseEnrollSerializer

class CourseRatingList(generics.ListCreateAPIView):
   queryset=models.CourseRating.objects.all()
   serializer_class=CourseRatingSerializer
   '''def get_queryset(self):
      course_id = self.kwargs['course_id']
      course = models.Course.objects.get(pk=course_id)
      return models.CourseRating.objects.filter(course=course)'''

def fetch_rating_status(request, learner_id, course_id):
   learner = models.Learner.objects.filter(id=learner_id).first()
   course= models.Course.objects.filter(id=course_id).first()
   ratingStatus=models.CourseRating.objects.filter(course=course,learner=learner).count()
   if ratingStatus:
      return JsonResponse({'bool':True})
   else:
      return JsonResponse({'bool':False})

@csrf_exempt
def tutor_change_password(request, tutor_id):
   password = request.POST['password']
   try:
      tutorData = models.Tutor.objects.get(id = tutor_id)
   except models.Tutor.DoesNotExist:
      tutorData=None
   if tutorData:
      models.Tutor.objects.filter(id=tutor_id).update(password=password)
      return JsonResponse({'bool':True})
   else:
      return JsonResponse({'bool':False})
