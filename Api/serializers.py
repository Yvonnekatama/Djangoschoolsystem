from django.db import models
from django.db.models import fields
from rest_framework import serializers
from student.models import Student
from trainer.models import Trainer
from course.models import Course
from events.models import Event

class StudenSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields =("first_name","last_name","age")

class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Trainer
        fields =("first_name","last_name","email_address")        

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Course
        fields =("course_name","course_code","course_trainer","course_description")

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model=Event
        fields ="__all__"