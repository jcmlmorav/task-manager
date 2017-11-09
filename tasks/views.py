from django.shortcuts import render, redirect
from django.template.defaultfilters import slugify
from .forms import ProjectForm
from .models import Project

def index(request):
    return render(request, 'tasks/index.html')

def home(request):
    if request.user.is_anonymous:
        return redirect( 'users.login' )

    projects = Project.objects.filter(user_id=request.user.id)

    return render(request, 'tasks/home.html', {'projects': projects})

def projects(request):
    if request.user.is_anonymous:
        return redirect( 'users.login' )

    projects = Project.objects.filter(user_id=request.user.id)

    return render(request, 'tasks/projects.html', {'projects': projects})

def projects_new(request):
    if request.user.is_anonymous:
        return redirect( 'users.login' )

    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user
            project.slug = slugify(project.name)
            project.save()
    else:
        form = ProjectForm()

    return render(request, 'tasks/projects_new.html', {'form': form})

def projects_view(request, slug):
    if request.user.is_anonymous:
        return redirect( 'users.login' )

    return render(request, 'tasks/projects_view.html', {'get': slug})
