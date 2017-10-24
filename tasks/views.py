from django.shortcuts import render, redirect

def index(request):
    return render(request, 'tasks/index.html')

def manage(request):
    if request.user.is_anonymous:
        return redirect( 'users.login' )
