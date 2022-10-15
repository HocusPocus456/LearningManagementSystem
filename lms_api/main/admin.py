from django.contrib import admin
from . import models

#1
admin.site.register(models.Tutor)
#2
admin.site.register(models.CourseCategory)
#3
admin.site.register(models.Course)
#4
admin.site.register(models.Chapter)
#5
admin.site.register(models.Learner)
#6
admin.site.register(models.LearnerCourseEnrollment)
#7
admin.site.register(models.LearnerFavouriteCourse)
#8
admin.site.register(models.CourseRating)
