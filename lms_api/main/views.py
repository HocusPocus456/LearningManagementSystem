from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework import generics
from rest_framework import permissions
from .serializers import TutorSerializer
from . import models
class TutorList(generics.ListCreateAPIView):
   queryset = models.Tutor.objects.all()
   serializer_class = TutorSerializer
   permission_classes = [permissions.IsAuthenticated]

class TutorDetail(generics.RetrieveUpdateDestroyAPIView):
   queryset = models.Tutor.objects.all()
   serializer_class = TutorSerializer
   permission_classes = [permissions.IsAuthenticated]
