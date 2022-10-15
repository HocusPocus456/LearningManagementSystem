from xml.sax.handler import feature_external_ges
from django.db import models
# Create your models here.
from pyexpat import model
from statistics import mode
from tabnanny import verbose
from django.db import models
from django.core import serializers
#import cv2 
#Tutor Model
class Tutor(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100,blank=True, null=True)
    qualification = models.CharField(max_length=200)
    mobile_no = models.CharField(max_length=13)
    profile_img=models.ImageField(upload_to='tutor_profile_imgs/', null=True)
    skills = models.TextField()

    class Meta:
        verbose_name_plural = "1. Tutors"

    def skill_list(self):
        skill_list = self.skills.split(',')
        return skill_list

#Total Tutor Courses
    def total_tutor_courses(self):
        total_courses = Course.objects.filter(tutor=self).count()
        return total_courses

#Total Tutor Chapters
    def total_tutor_chapters(self):
        total_chapters = Chapter.objects.filter(course__tutor=self).count()
        return total_chapters

#Total Tutor Learners
    def total_tutor_learners(self):
        total_learners = LearnerCourseEnrollment.objects.filter(course__tutor=self).count()
        return total_learners
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
    tutor = models.ForeignKey(Tutor, on_delete = models.CASCADE, related_name="tutor_courses")
    title = models.CharField(max_length=150)
    description = models.TextField() 
    featured_img = models.ImageField(upload_to='course_imgs/', null=True)
    techs = models.TextField(null=True) 
    class Meta:
        verbose_name_plural = "3. Courses"

    def related_videos(self):
        related_videos=Course.objects.filter(techs__icontains=self.techs).exclude(id=self.id)
        return serializers.serialize('json',related_videos)

    def tech_list(self):
        tech_list = self.techs.split(',')
        return tech_list

    def total_enrolled_learners(self):
        total_enrolled_learners=LearnerCourseEnrollment.objects.filter(course=self).count()
        return total_enrolled_learners

    def course_rating(self):
        course_rating=CourseRating.objects.filter(course=self).aggregate(avg_rating=models.Avg('rating'))
        return course_rating['avg_rating']

    def __str__(self):
        return self.title

#Chapter Model
class Chapter(models.Model):
    course = models.ForeignKey(Course, on_delete = models.CASCADE, related_name='course_chapters')
    title = models.CharField(max_length=150)
    description = models.TextField() 
    video = models.FileField(upload_to='chapter_videos/', null=True)
    remarks = models.TextField(null=True) 
    class Meta:
        verbose_name_plural = "4. Chapters"

    '''def chapter_duration(self):
        seconds = 0
        import cv2
        cap = cv2.VideoCapture(self.video.path)
        fps = cap.get(cv2,CAP_PROP_FPS)
        frame_count = int(cap.get(cv2,CAP_PROP_FRAME_COUNT))
        if frame_count:
            duration = frame_count/fps
            print('fps =' + str(fps))
            print('number of frames = '+ str(frame_count))
            print('duration (S) = '+str(duration))
            minutes = int(duration/60)
            seconds = duration%60
            print('duration (M:S) = '+ str(minutes)+':' + str(seconds) )
        return seconds
'''
#Learner Model
class Learner(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    username = models.CharField(max_length=200)
    interested_subjects = models.TextField()

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name_plural = "5. Learners"

# LearnerCourseEnrollment
class LearnerCourseEnrollment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    learner = models.ForeignKey(Learner,on_delete=models.CASCADE)
    enrolled_time=models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural ="6. Enrolled Courses"

    def __str__(self):
        return f"{self.course}-{self.learner}"

#Learner Favourite Course
class LearnerFavouriteCourse(models.Model):
    course=models.ForeignKey(Course, on_delete=models.CASCADE)
    learner = models.ForeignKey(Learner, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural ="7. Learner Favourite Courses"

    def __str__(self):
        return f"{self.course}-{self.learner}"

#Course Rating and Review
class CourseRating(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    learner = models.ForeignKey(Learner,on_delete=models.CASCADE, null=True)
    rating = models.PositiveBigIntegerField(default=0)
    reviews = models.TextField(null=True)
    review_time=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural ="8. Learner Favourite Courses"

    def __str__(self):
        return f"{self.course}-{self.learner}-{self.rating}"