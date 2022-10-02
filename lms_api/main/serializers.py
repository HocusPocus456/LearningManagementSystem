from rest_framework import serializers
from . import models

class TutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tutor
        fields = ['id','full_name','email','password','qualification','mobile_no','skills','profile_img','tutor_courses']
        depth=1
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CourseCategory
        fields = ['id','title','description']

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields = ['id','category','tutor','title','description','featured_img','techs','course_chapters','related_videos']
        depth=1

class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Chapter
        fields = ['id','course','title','description','video','remarks']

class LearnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Learner
        fields = ['full_name','email','password','username','interested_subjects']