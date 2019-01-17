from django.contrib import admin
from users.models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_info', 'city', 'website')

    def user_info(self, obj):
        return obj.about_me

    def get_queryset(self, request):
        queryset = super(CustomUserAdmin, self).get_queryset(request)
        queryset = queryset.order_by('user')
        return queryset

    user_info.short_description = 'Info'


admin.site.register(CustomUser, CustomUserAdmin)
