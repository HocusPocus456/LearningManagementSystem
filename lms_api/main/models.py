from django.db import models
# Create your models here.
from pyexpat import model
from statistics import mode
from tabnanny import verbose
from django.db import models
#Tutor Model
class Tutor(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    qualification = models.CharField(max_length=200)
    mobile_no = models.CharField(max_length=13)
    skills = models.TextField()

    class Meta:
        verbose_name_plural = "1. Tutors"

#Course Category model
class CourseCategory(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()

    class Meta:
        verbose_name_plural = "2. Course Categories"

    def __str__(self):
        return self.title
#Course Model
class Course(models.Model):
    category = models.ForeignKey(CourseCategory, on_delete = models.CASCADE)
    tutor = models.ForeignKey(Tutor, on_delete = models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.TextField() 
    featured_img = models.ImageField(upload_to='course_imgs/', null=True)
    techs = models.TextField(null=True) 
    class Meta:
        verbose_name_plural = "3. Courses"

#Learner Model
class Learner(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    qualification = models.CharField(max_length=200)
    mobile_no = models.CharField(max_length=13)
    address = models.TextField()
    interested_categories = models.TextField()

    class Meta:
        verbose_name_plural = "4. Learners"