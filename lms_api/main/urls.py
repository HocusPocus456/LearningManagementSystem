from ast import pattern
from django.urls import path
from . import views
urlpatterns = [
    # Tutor
    path('tutor/', views.TutorList.as_view()),
    path('tutor/dashboard/<int:pk>/', views.TutorDashboard.as_view()),
    path('tutor/<int:pk>/', views.TutorDetail.as_view()),
    path('tutor/change-password/<int:tutor_id>/', views.tutor_change_password),
    path('tutor-login', views.tutor_login),

    #Category
    path('category/', views.CategoryList.as_view()),

    #Course
    path('course/', views.CourseList.as_view()),
    

    #Course Detail
    path('course/<int:pk>/', views.CourseDetailView.as_view()),

    #Specific Courses
    path('course-chapters/<int:course_id>', views.CourseChapterList.as_view()),

    #Chapter
    path('chapter/<int:pk>', views.ChapterDetailView.as_view()),

    #Teacher Courses
    path('tutor-courses/<int:tutor_id>', views.TutorCourseList.as_view()),

    #Course Detail
    path('tutor-course-detail/<int:pk>', views.TutorCourseDetail.as_view()),

    
    #Learner 
    path('learner/', views.LearnerList.as_view()),
    path('learner-login',views.learner_login),
    path('learner-enroll-course/', views.LearnerEnrollCourseList.as_view()),
    path('fetch-enroll-status/<int:learner_id>/<int:course_id>',views.fetch_enroll_status),
    path('fetch-all-enrolled-learners/<int:tutor_id>/',views.EnrolledLearnerList.as_view()),
    path('fetch-enrolled-learners/<int:course_id>',views.EnrolledLearnerList.as_view()),
    path('fetch-enrolled-courses/<int:learner_id>',views.EnrolledLearnerList.as_view()),
    path('fetch-recommended-courses/<int:learnerId>',views.CourseList.as_view()),
    path('fetch-rating-status/<int:learner_id>/<int:course_id>',views.fetch_rating_status),
    path('course-rating/', views.CourseRatingList.as_view()),
    path('learner-add-favourite-course/', views.LearnerFavouriteCourseList.as_view()),    
    path('learner-remove-favourite-course/<int:course_id>/<int:learner_id>', views.remove_favourite_course),
    path('fetch-favourite-status/<int:learner_id>/<int:course_id>',views.fetch_favourite_status),
    path('fetch-favourite-courses/<int:learner_id>',views.LearnerFavouriteCourseList.as_view()),



]
