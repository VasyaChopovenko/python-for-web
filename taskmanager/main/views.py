from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')


def resume_en(request):
    return render(request, 'main/resumeEN.html')


def resume_ua(request):
    return render(request, 'main/resumeUA.html')


def creative_resume(request):
    return render(request, 'main/creativeResume.html')
