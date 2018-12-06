from django.db import models


# Create your models here.
class Genre(models.Model):
    genre = models.CharField()
    desciption = models.TextField()


class Book(models.Model):
    genre_id = models.Foreignkey('Genre', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    isbn = models.IntegerField()
    published_year = models.DateField()
    cover_picture = models.ImageField(upload_to='pic_path',
                                      default='pic_path_for_default_pic')
    publisher = models.CharField(max_length=100)
    no_of_pages = models.IntegerField()


class Author(models.Model):
    name = models.CharField(max_length=100)
    website = models.CharField(blank=True)
    twitter_id = models.CharField(blank=True)
    member_since = models.DateField()
    story = models.TextField()


class BookAuthor(models.Model):
    book_id = models.Foreignkey('Book', on_delete=models.CASCADE)
    author_id = models.Foreignkey('Author', on_delete=models.CASCADE)
