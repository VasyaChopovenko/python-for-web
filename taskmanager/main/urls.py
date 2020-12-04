from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('resumeEN', views.resume_en, name='resumeEN'),
    path('resumeUA', views.resume_ua, name='resumeUA'),
]