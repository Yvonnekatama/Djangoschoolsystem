from django.conf.urls import url
from . import views

app_name = 'events'
urlpatterns = [
  
    url(r'^calendar/$', views.CalendarView.as_view(), name='calendar'), 
    url(r'^eventform/$', views.event, name='eventform'), 

    
]