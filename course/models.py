from django.db import models

# Create your models here.
class Course(models.Model):
  course_name=models.CharField(max_length=20)  
  course_code=models.CharField(max_length=20)
  course_channel=models.CharField(max_length=20)
  course_trainer=models.CharField(max_length=20)
  course_description=models.CharField(max_length=100)
  course_syllabus=models.FileField(upload_to ='files/')