from django.conf.urls import url
from . import views

app_name = 'student'
urlpatterns = [
    #/student/
    url(r'^$', views.index, name='index'),
]