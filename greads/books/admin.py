from django.contrib import admin
from books.models import Book, Author, Genre, UserBook

# Register your models here.
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(UserBook)
