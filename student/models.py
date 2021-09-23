import django
from django.db import models
import datetime
from django.core.validators import MinValueValidator,MaxValueValidator

def current_year():
    return datetime.date.today().year

def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)

# Create your models here.
Gender=(
    ('MALE','MALE'),
    ('FEMALE','FEMALE')
)
Nationality=(
    ('KENYAN','KENYAN'),
    ('UGANDAN','UGANDAN'),
    ('SUDAN','SUDAN'),
    ('RWANDESE','RWANDESE'),
)

class Student(models.Model):
    first_name=models.CharField(max_length=12)
    last_name=models.CharField(max_length=20)
    age=models.PositiveSmallIntegerField()
    date_of_birth=models.DateField(default='2000-10-12')
    phone_number=models.CharField(max_length=20)
    admission_date=models.DateField(default='YYYY-MM-DD')
    guardian_name=models.CharField(max_length=20)
    id_number=models.CharField(max_length=20)
    nationality=models.CharField(max_length=20,choices=Nationality,default='KENYAN')
    class_name=models.CharField(max_length=20,null=True,blank=True)
    medical_report=models.FileField(upload_to ='files/')
    email=models.EmailField()
    academic_year=models.IntegerField(default=current_year(),validators=[MinValueValidator(1984),max_value_current_year])
    gender=models.CharField(max_length=20,choices=Gender,default='FEMALE')
    city=models.CharField(max_length=20)
    image=models.ImageField(upload_to='images/')


