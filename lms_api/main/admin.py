from django.contrib import admin
from . import models

admin.site.register(models.Tutor)
admin.site.register(models.CourseCategory)
admin.site.register(models.Course)
admin.site.register(models.Learner)