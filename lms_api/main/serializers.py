from dataclasses import field
from rest_framework import serializers
from rest_framework.response import Response
from . import models

class TutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tutor
        fields = ['id','full_name','email','password','qualification','mobile_no','skills','skill_list','profile_img','tutor_courses']
    def __init__(self, *args, **kwargs):
        super(TutorSerializer,self).__init__(*args,**kwargs)
        request = self.context.get('request')
        self.Meta.depth = 0
        if request and request.method == 'GET':
            self.Meta.depth = 1

class TutorDashboardSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Tutor
        fields = ['total_tutor_courses', 'total_tutor_learners','total_tutor_chapters']    

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CourseCategory
        fields = ['id','title','description']

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields = [
            'id',
            'category',
            'tutor',
            'title',
            'description',
            'featured_img',
            'techs',
            'course_chapters',
            'related_videos',
            'tech_list',
            'total_enrolled_learners',
            'course_rating'
            ]
    def __init__(self, *args, **kwargs):
        super(CourseSerializer,self).__init__(*args,**kwargs)
        request = self.context.get('request')
        self.Meta.depth = 0
        if request and request.method == 'GET':
            self.Meta.depth = 2
class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Chapter
        fields = ['id','course','title','description','video','remarks']#'chapter_duration',

class LearnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Learner
        fields = ['full_name','email','password','username','interested_categories']

class LearnerCourseEnrollSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LearnerCourseEnrollment
        fields = ['id','course','learner','enrolled_time']
    def __init__(self, *args, **kwargs):
        super(LearnerCourseEnrollSerializer,self).__init__(*args,**kwargs)
        request = self.context.get('request')
        self.Meta.depth = 0
        if request and request.method == 'GET':
            self.Meta.depth = 1

class CourseRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CourseRating
        fields = ['id','course','learner','rating','reviews','review_time']
    def __init__(self, *args, **kwargs):
        super(CourseRatingSerializer,self).__init__(*args,**kwargs)
        request = self.context.get('request')
        self.Meta.depth = 0
        if request and request.method == 'GET':
            self.Meta.depth = 1