from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=100, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    about_me = models.TextField(max_length=500, blank=True)
    website = models.URLField(default='', blank=True)

    def __str__(self):
        return self.user.username


'''def create_profile(sender, kwargs):
    if kwargs['created']:
        custom_user = CustomUser.objects.create(user=kwargs['instance'])
    post_save.connect(create_profile, sender=User)

        '''


@receiver(post_save, sender=User)
def create_or_update_user_customuser(sender, instance, created, **kwargs):
    if created:
        CustomUser.objects.create(user=instance)
    instance.customuser.save()


'''
# Create your models here.
class User(models.Model):
    email = models.EmailField(primary_key=True)
    username = models.CharField(max_length=100)
    password = models.CharField()
    date_joined = models.DateField()
    birthday = models.DateField(blank=True)
    display_picture = models.ImageField(upload_to='pic_path',
                                        default='pic_path_for_default_pic')


class UserBook(models.Model):
    email_id = models.Foreignkey('User', on_delete=models.CASCADE)
    book_id = models.Foreignkey('Book', on_delete=models.CASCADE)
    rating = models.DoubleField()
    shelf = models.CharField()
    date_added = models.DateTimeField()


class Notification(models.Model):
    email_id = models.Foreignkey('User', on_delete=models.CASCADE)
    notifications = models.CharField()
    start_date = models.DateField()
    end_date = models.DateField()
    due_date = models.DateField()
    pending = models.BooleanField()
'''
