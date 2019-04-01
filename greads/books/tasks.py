# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task
from celery import Celery
import requests
from xml.etree import ElementTree
from django.db.models import Q

app = Celery('tasks', broker='amqp://lakha:pooja123@localhost:5672/djhost')


@shared_task
def add(x, y):
    return x + y


@shared_task
def update_book_cover_summary():
    from .models import Book

    books = Book.objects.filter(Q(summary="") | Q(cover_picture="")).values('isbn')
    for book in books:
        isbn = book['isbn']
        key = 'xXmFRqAwrnJKqDaOPBT2A'
        response = requests.get("https://www.goodreads.com/book/isbn/" + isbn + "?key=" + key)
        tree = ElementTree.fromstring(response.content)
        book_update = Book.objects.get(isbn=isbn)
        cover_pic = tree[1][8].text
        book_summary = tree[1][16].text
        book_update.cover_picture = cover_pic
        book_update.summary = book_summary
        book_update.save()
