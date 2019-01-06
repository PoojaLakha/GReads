from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render
from django.urls import reverse_lazy

from .models import Book


# Create your views here.


def index(request):
    return render(request, 'books/index.html')


class BookCreate(CreateView):
    model = Book
    fields = '__all__'


class BookUpdate(UpdateView):
    model = Book
    fields = '__all__'


def BookConfirm(request, pk=Book.isbn):
    name = Book.objects.get(isbn=pk)
    isbn = pk
    context = {
        'name': name,
        'isbn': isbn
    }
    return render(request, 'books/book_confirm_delete.html',
                  context)


class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('books:books')


class BookListView(generic.ListView):
    model = Book
    template_name = 'books/book_list.html'

    def get_queryset(self):
        book_list = Book.objects.all()
        return book_list


class BookDetailView(generic.DetailView):
    model = Book


'''
class AuthorAdd(CreateView):
    model = Author
    fields = '__all__'


class AuthorUpdate(UpdateView):
    model = Author
    fields = '__all__'


class AuthorDelete(DeleteView):
    model = Author
    success_url = reverse_lazy('authors')'''
