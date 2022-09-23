from rest_framework import serializers
from . import models
from django.core.mail import send_mail
class TutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tutor
        fields = ['id','full_name','email','password','qualification','mobile_no','skills','otp_digit']

    def __init__(self, *args, **kwargs):
        super(TutorSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        self.Meta.depth = 0
        if request and request.method == 'GET':
            self.Meta.depth = 1
    def create(self,validate_data):
        email = self.validated_data['email']
        otp_digit = self.validated_data['otp_digit']
        instance = super(TutorSerializer, self).create(validate_data)
        send_mail(
                'Verify Account',
                'Please verify your account.',
                'asheetal002@gmail.com',
                [email],
                fail_silently=False,
                html_message=f'<p>Your otp is: </p><p>{otp_digit}</p>'
            )
        return instance

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CourseCategory
        fields = ['id','title','description']

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields = ['id','category','tutor','title','description','featured_img','techs']

