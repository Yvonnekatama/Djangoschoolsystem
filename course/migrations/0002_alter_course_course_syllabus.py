# Generated by Django 3.2.5 on 2021-08-20 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_syllabus',
            field=models.FileField(upload_to='files/'),
        ),
    ]