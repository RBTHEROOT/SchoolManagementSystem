from django.conf.urls import url
from . import views

app_name = 'student'
urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'student/all/$', views.AllStudents, name='all'),
    #/student/
    url(r'student/admission/new/$', views.AdmissionCrate.as_view(), name='admission-add'),
    url(r'student/edit/(?P<pk>[0-9]+)/$', views.AdmissionUpdate.as_view(), name='admission-update'),

    url(r'class/new/$', views.StdCreate.as_view(), name='std-add'),
    url(r'class/edit/(?P<pk>[0-9]+)/$', views.StdUpadate.as_view(), name='std-update'),
    url(r'class/(?P<pk>[0-9]+)delete/$', views.StdUpadate.as_view(), name='std-delete'),

    url(r'feetype/new/$', views.FeeTypeCreate.as_view(), name='feetype-add'),
    url(r'feetype/edit/(?P<pk>[0-9]+)/$', views.FeeTypeUpdate.as_view(), name='feetype-update'),


    url(r'feestrucutre/new/$', views.FeeStructureCreate.as_view(), name='feestrucutre-add'),
    url(r'feestrucutre/edit/(?P<pk>[0-9]+)/$', views.FeeStructureUpdate.as_view(), name='feestrucutre-update'),


    url(r'feereceived/new/$', views.FeeReceivedCreate.as_view(), name='feereceived-add'),
    url(r'feereceived/edit/(?P<pk>[0-9]+)/$', views.FeeReceivedUpdate.as_view(), name='feereceived-update'),

]