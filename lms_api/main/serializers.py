from rest_framework import serializers
from . import models

class TutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tutor
        fields = ['id','full_name','email','password','qualification','mobile_no','skills']
