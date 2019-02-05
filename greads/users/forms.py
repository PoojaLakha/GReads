from django.contrib.auth.forms import UserChangeForm
from users.models import CustomUser


class EditProfileForm(UserChangeForm):
    template_name = '/users/edit_profile.html'

    class Meta:
        model = CustomUser
        fields = (
            'user',
            'city',
            'birth_date',
            'about_me',
            'website'
        )
