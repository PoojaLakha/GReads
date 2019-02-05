# from django.views import generic
from django.urls import reverse
from django.shortcuts import render, redirect
from users.forms import EditProfileForm
# from django.views.generic.edit import UpdateView
from django.contrib.auth.models import User

# from .models import CustomUser


# Create your views here.
def view_profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user}
    return render(request, 'users/profile.html', args)


def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect(reverse('users:view_profile'))
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'users/edit_profile.html', args)
