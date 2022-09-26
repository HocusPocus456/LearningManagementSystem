from ast import pattern
from django.urls import path
from . import views
urlpatterns = [
    # Tutor
    path('tutor/', views.TutorList.as_view()),
    path('tutor/<int:pk>/', views.TutorDetail.as_view()),
    path('tutor-login', views.tutor_login),

    #Category
    path('category/', views.CategoryList.as_view()),

    #Course
    path('course/', views.CourseList.as_view()),

    #Chapter
    path('chapter/', views.ChapterList.as_view()),

    #Teacher Courses
    path('tutor-courses/<int:tutor_id>', views.TutorCourseList.as_view()),

    #Specific Courses
    path('course-chapters/<int:course_id>', views.CourseChapterList.as_view()),

    #Course Detail
    path('tutor-course-detail/<int:pk>', views.TutorCourseDetail.as_view()),

]