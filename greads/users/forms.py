from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
# from users.models import CustomUser


class EditProfileForm(UserChangeForm):
    template_name = '/users/edit_profile.html'

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'password',
        )
