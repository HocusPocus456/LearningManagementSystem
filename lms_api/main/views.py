from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework import generics
from rest_framework import permissions
from .serializers import TutorSerializer
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
      return JsonResponse({'bool':True})
   else:
      return JsonResponse({'bool':False})