from django.shortcuts import render
from django.http import HttpResponse

def ourteam_view(request):
    return render(request,'pages/team.html')

def testimonial_view(request):
    return render(request,'pages/testimonial.html')

def fourpage_view(request):
    return render(request,'pages/404.html')


