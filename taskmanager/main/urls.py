from django.urls import path
from . import views

urlpatterns = [
    path('', views.resume, name='resume'),
    path('resume-en', views.resume_en, name='resume-en'),
    path('resume-ua', views.resume_ua, name='resume-ua'),
]