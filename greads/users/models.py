from django.db import models

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
