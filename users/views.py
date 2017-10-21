from django.shortcuts import render, redirect
from users.forms import EditProfileForm
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users.profile')
    else:
        form = UserCreationForm()

    args = {
        'form': form
    }
    return render(request, 'accounts/register.html', args)

def login(request):
    pass

def profile(request):
    if not request.user.username:
        return redirect( 'users.login' )

    args = { 'user': request.user }
    return render(request, 'accounts/profile.html', args)

def edit_profile(request):
    if( request.method == 'POST'):
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('users.profile')
    else:
        form = EditProfileForm(instance=request.user)

    args = {
        'form': form
    }
    return render(request, 'accounts/edit_profile.html', args)

def change_password(request):
    if( request.method == 'POST'):
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('users.profile')
        else:
            return redirect('users.change_password')
    else:
        form = PasswordChangeForm(user=request.user)

    args = {
        'form': form
    }
    return render(request, 'accounts/change_password.html', args)
