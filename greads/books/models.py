from django.db import models
from django.urls import reverse


# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=200)
    # desciption = models.TextField()

    def __str__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    # website = models.CharField(blank=True)
    # twitter_id = models.CharField(blank=True)
    # member_since = models.DateField()
    # about = models.TextField()

    def __str__(self):
        return '{0} {1}'.format(self.first_name, self.last_name)


class Book(models.Model):
    isbn = models.CharField(max_length=13, primary_key=True)
    title = models.CharField(max_length=200)
    author = models.ManyToManyField(Author)
    genre = models.ManyToManyField(Genre)
    summary = models.TextField()
    # published_year = models.DateField()
    # cover_picture = models.ImageField(upload_to='pic_path',
    #                                   default='pic_path_for_default_pic')
    # publisher = models.CharField(max_length=100)
    # no_of_pages = models.IntegerField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('books:books')


'''
class BookAuthor(models.Model):
    book_id = models.Foreignkey('Book', on_delete=models.CASCADE)
    author_id = models.Foreignkey('Author', on_delete=models.CASCADE)
'''
