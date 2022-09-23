from statistics import mode
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework import generics
from rest_framework import permissions
from .serializers import TutorSerializer, CategorySerializer, CourseSerializer
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
      if not tutorData.verify_status:
         return JsonResponse({'bool':False,'msg':'Account is not verified!'})
      else:
         return JsonResponse({'bool':True,'tutor_id':tutorData.id})
   else:
      return JsonResponse({'bool':False, 'msg':'Invalid Email or Password!!!'})

@csrf_exempt
def verify_tutor_via_otp(request, tutor_id):
   otp_digit = request.POST.get('otp_digit')
   verify = models.Tutor.objects.filter(id=tutor_id, otp_digit=otp_digit).first()
   if verify:
      models.Tutor.objects.filter(id=tutor_id, otp_digit=otp_digit).update(verify_status=True)
      return JsonResponse({'bool':True, 'tutor_id':verify.id})
   else:
      return JsonResponse({'bool':False})
class CategoryList(generics.ListCreateAPIView):
   queryset = models.CourseCategory.objects.all()
   serializer_class = CategorySerializer

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
