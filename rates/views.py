from django.shortcuts import render,redirect
from .models import *
from .forms import ProjectUpload,UpdateProfileForm
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets


def home(request):
    projects = Post.objects.all()
    return render(request, 'projects/index.html', {"projects":projects})



