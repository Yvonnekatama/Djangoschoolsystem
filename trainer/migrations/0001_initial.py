# Generated by Django 3.2.5 on 2021-08-13 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=12)),
                ('last_name', models.CharField(max_length=20)),
                ('course', models.CharField(max_length=20)),
                ('email_address', models.EmailField(max_length=25)),
                ('id_number', models.CharField(max_length=20)),
                ('contract', models.FileField(upload_to='files/')),
                ('resume', models.FileField(upload_to='files/')),
                ('Salary', models.PositiveBigIntegerField()),
                ('image', models.ImageField(upload_to='images/')),
                ('relationship_syllabus', models.CharField(max_length=25)),
                ('phone_number', models.CharField(max_length=25)),
                ('gender', models.CharField(choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE')], default='FEMALE', max_length=25)),
                ('Company', models.CharField(max_length=25)),
                ('joining_date', models.DateField(default='2000-10-12')),
            ],
        ),
    ]
