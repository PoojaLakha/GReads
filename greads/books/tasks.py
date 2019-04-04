from __future__ import absolute_import, unicode_literals
from celery import shared_task
from celery import Celery
import requests
import os
from xml.etree import ElementTree

cloudamqp_url = os.environ.get('CLOUDAMQP_URL')
app = Celery('tasks', broker=cloudamqp_url)


# Create your tasks here
@shared_task
def add(x, y):
    return x + y


@shared_task
def update_book_cover_summary(f_isbn):
    from .models import Book
    isbn = f_isbn
    key = os.environ.get('GOODREADS_KEY')
    response = requests.get("https://www.goodreads.com/book/isbn/" + isbn + "?key=" + key)
    tree = ElementTree.fromstring(response.content)
    book_update = Book.objects.get(isbn=isbn)
    cover_pic = tree[1][8].text
    book_summary = tree[1][16].text
    book_update.cover_picture = cover_pic
    book_update.summary = book_summary
    book_update.save()
