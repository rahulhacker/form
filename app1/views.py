from django.http import HttpResponse
from django.shortcuts import render
from .models import Profile


def index(request):
    return render(request, 'index.html')

def save(request):
    print request.FILES
    print request.POST["name"]
    instance = Profile(name=request.POST["name"],email=request.POST["email"],resume=request.FILES['resume'])
    instance.save()
    return render(request, 'index.html')