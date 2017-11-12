from django.shortcuts import render, redirect, get_object_or_404
from django.template.defaultfilters import slugify
from .forms import ProjectForm, StageForm
from .models import Project, Stage

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
            return redirect('tasks.projects')
    else:
        form = ProjectForm()

    return render(request, 'tasks/projects_new.html', {'form': form})

def projects_view(request, slug):
    if request.user.is_anonymous:
        return redirect( 'users.login' )

    project = get_object_or_404(Project, slug=slug)
    stages = Stage.objects.filter(project=project)

    return render(request, 'tasks/projects_view.html', {
        'project': project,
        'stages': stages
    })

def stages_new(request, project_slug):
    if request.user.is_anonymous:
        return redirect( 'users.login' )

    if request.method == 'POST':
        form = StageForm(request.POST)
        if form.is_valid():
            current_project = Project.objects.get(slug=project_slug,user_id=request.user.id)
            stage = form.save(commit=False)
            stage.project = current_project
            stage.save()
            return redirect('tasks.projects_view', slug=current_project.slug)
    else:
        form = StageForm()

    return render(request, 'tasks/stages_new.html', {'form': form})
