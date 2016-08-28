from django.conf.urls import url
from . import views

app_name = 'student'
urlpatterns = [
    #/student/
    url(r'^$', views.IndexView.as_view(), name='index'),

]