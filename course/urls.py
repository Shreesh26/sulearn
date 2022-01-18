from unicodedata import name
from django.urls import path

from course.models import certificate
from . import views

urlpatterns=[
    path('', views.home, name='home'),
    path("educator/", views.educator, name='educator'),
    path('edu_submit/', views.edu_submit, name='edu_submit'),
    path('details/', views.usr_detail, name="usr_details"),
    path('add_course/', views.add_course, name="add_course"),
    path('course_page/', views.coursePage, name="coursePage"),
    path('course/', views.courseView, name='courseView'),
    path('enroll/', views.enroll, name='enroll'),
    path('certificate/', views.certificate, name='certificate'),
    path('certificate_page/', views.certification, name='proof'),
    path('view_certificate/', views.view_certificate, name='view'),
    path('search/', views.search, name='search'),

]