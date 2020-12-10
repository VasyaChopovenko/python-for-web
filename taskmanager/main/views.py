from django.shortcuts import render


def resume_en(request):
    return render(request, 'main/resume-en.html')


def resume_ua(request):
    return render(request, 'main/resume-ua.html')
