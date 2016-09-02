from django.conf.urls import url,include
from django.contrib import admin
from . import views
from student import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'', include('student.urls'))
]
