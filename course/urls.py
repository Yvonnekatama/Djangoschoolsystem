
from django.urls import path
from .views import view_course
from django.conf import settings
from django.conf.urls.static import static
from .views import course_list
app_name='course'
urlpatterns=[
    path("register/",view_course,name="View Courses"),
    path("list/", course_list, name = "Courses_list")
]
