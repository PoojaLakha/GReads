from django.views import generic
from django.views.generic.edit import UpdateView, DeleteView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from .models import Book, Author, Genre
from .forms import BookForm, AuthorForm, GenreForm


# Create your views here.


def index(request):
    return render(request, 'books/index.html')


def new_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.save()
            books = Book.objects.all()
            return render(request, 'books/book_list.html',
                          {'books': books})
    else:
        form = BookForm()
        # print("Else")
    return render(request, 'books/bookform.html', {'form': form})


'''class BookCreate(CreateView):
    model = Book
    fields = '__all__'
'''


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
class BookUpdate(UpdateView):
    model = Book
    fields = '__all__'
'''


def new_author(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            author = form.save(commit=False)
            author.save()
            # authors = Author.objects.all()
            # return render(request, 'books/bookform.html',
            #               {'authors': authors})
            next = request.POST.get('next', '/')
            return HttpResponseRedirect(next)
    else:
        form = AuthorForm()
        # print("Else")
    # return HttpResponseRedirect(next)

    return render(request, 'books/authorform.html', {'form': form})


class AuthorUpdate(UpdateView):
    model = Book
    fields = '__all__'


def AuthorConfirm(request, pk=Author.id):
    name = Author.objects.get(book_id=pk)
    book_id = pk
    context = {
        'name': name,
        'id': book_id
    }
    return render(request, 'books/author_confirm_delete.html',
                  context)


class AuthorDelete(DeleteView):
    model = Author
    success_url = reverse_lazy('books:books')


def new_genre(request):
    if request.method == "POST":
        form = GenreForm(request.POST)
        if form.is_valid():
            genre = form.save(commit=False)
            genre.save()
            # authors = Author.objects.all()
            # return render(request, 'books/bookform.html',
            #               {'authors': authors})
            next = request.POST.get('next', '/')
            return HttpResponseRedirect(next)
    else:
        form = GenreForm()
        # print("Else")
    # return HttpResponseRedirect(next)

    return render(request, 'books/genreform.html', {'form': form})


class GenreUpdate(UpdateView):
    model = Book
    fields = '__all__'


def GenreConfirm(request, pk=Genre.id):
    name = Genre.objects.get(book_id=pk)
    book_id = pk
    context = {
        'name': name,
        'id': book_id
    }
    return render(request, 'books/genre_confirm_delete.html',
                  context)


class GenreDelete(DeleteView):
    model = Author
    success_url = reverse_lazy('books:books')
