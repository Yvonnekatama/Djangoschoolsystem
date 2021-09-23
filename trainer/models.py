import django
from django.db import models
import datetime

def current_year():
    return datetime.date.today().year
Gender=(
    ('MALE','MALE'),
    ('FEMALE','FEMALE'),
)


# Create your models here.
class Trainer(models.Model):
    first_name=models.CharField(max_length=12)
    last_name=models.CharField(max_length=20)
    course=models.CharField(max_length=20)
    email_address= models.EmailField(max_length = 25)
    id_number=models.CharField(max_length=20)
    contract=models.FileField(upload_to ='files/')
    resume=models.FileField(upload_to ='files/')
    Salary=models.PositiveBigIntegerField()
    image=models.ImageField(upload_to='images/')
    relationship_syllabus=models.CharField(max_length = 25)
    phone_number=models.CharField(max_length = 25)
    gender=models.CharField(max_length = 25 ,choices=Gender,default='FEMALE')
    Company=models.CharField(max_length = 25)
    joining_date=models.DateField(default='2000-10-12')
    

