
from django.urls import path
from .views import register_student
from django.conf import settings
from django.conf.urls.static import static
from .views import trainer_list
app_name='trainer'
urlpatterns = [
    path("register/", register_student,name = "register_student"),
    path("list/", trainer_list, name = "trainer_list"),

]