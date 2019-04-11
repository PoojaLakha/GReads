from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.shortcuts import render

from .forms import UserForm, ProfileForm
from .forms import SignUpForm


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()

    return render(request, 'signup.html', {'form': form})


def view_profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user}
    return render(request, 'accounts/profile.html', args)


@login_required
def edit_profile(request):
    if request.method == 'POST':
        update_user_form = UserForm(request.POST, instance=request.user)
        update_profile_form = ProfileForm(request.POST,
                                          instance=request.user.profile)
        if update_user_form.is_valid() and update_profile_form.is_valid():
            user = update_user_form.save()
            profile = update_profile_form.save(commit=False)
            profile.user = user

            if 'avatar' in request.FILES:
                profile.avatar = request.FILES['avatar']

            profile.save()

            return redirect('accounts:view_profile')
    else:
        update_user_form = UserForm(instance=request.user)
        update_profile_form = ProfileForm(instance=request.user.profile)

    return render(request, 'accounts/edit_profile.html', {
        'update_user_form': update_user_form,
        'update_profile_form': update_profile_form
    })
