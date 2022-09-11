from ast import pattern
from django.urls import path
from . import views
urlpatterns = [
    path('tutor/', views.TutorList.as_view()),
    path('tutor/<int:pk>/', views.TutorDetail.as_view()),
]