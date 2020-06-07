from django.shortcuts import render,redirect
from .models import *
from .forms import ProjectUpload,UpdateProfileForm
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets


def home(request):
    projects = Post.objects.all()
    return render(request, 'projects/index.html', {"projects":projects})


@login_required (login_url='/accounts/login/?next=/')   
def new_project(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProjectUpload(request.POST,request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = current_user
            project.save()
        return redirect('home')
    else:
        form = ProjectUpload()
        return render(request,'projects/new_post.html',{"form":form}) 


