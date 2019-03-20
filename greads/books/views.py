from django.views import generic
from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic import ListView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Book, Author, Genre
from .forms import BookForm, AuthorForm, GenreForm
from .search import BookIndex


# Create your views here.
def es_search(request):
    template = 'books/book_list.html'

    query = request.GET.get('q')

    if query:
        s = BookIndex.search().query("match", title=query)
        response = s.execute()
        response_dict = response.to_dict()
        hits = response_dict['hits']['hits']
        titles = [hit['_source']['title'] for hit in hits]

    return render(request, template, {'titles': titles})


def search(request):
    template = 'books/search_book_list.html'
    page = request.GET.get('page', 1)

    query = request.GET['q']
    search_list = Book.objects.filter(title__icontains=query)

    paginator = Paginator(search_list, 5)
    try:
        search_list = paginator.page(page)
    except PageNotAnInteger:
        search_list = paginator.page(1)
    except EmptyPage:
        search_list = paginator.page(paginator.num_pages)

    return render(request, template, {'search_list': search_list,
                                      'query': query})


def genresearch(request):
    template = 'books/search_genre.html'

    query = request.GET['q']
    search_list = Book.objects.filter(genre__name__icontains=query).distinct()

    return render(request, template, {'search_list': search_list,
                                      'query': query})


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
    return render(request, 'books/bookform.html', {'form': form})


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
    context_object_name = 'book_list'
    paginate_by = 3
    queryset = Book.objects.all()


class BookDetailView(generic.DetailView):
    model = Book


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


def AuthorConfirm(request, pk=Author.id):
    name = Author.objects.get(book_id=pk)
    book_id = pk
    context = {
        'name': name,
        'id': book_id
    }
    return render(request, 'books/author_confirm_delete.html',
                  context)


class AuthorUpdate(UpdateView):
    model = Book
    fields = '__all__'


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


def GenreConfirm(request, pk=Genre.id):
    name = Genre.objects.get(book_id=pk)
    book_id = pk
    context = {
        'name': name,
        'id': book_id
    }
    return render(request, 'books/genre_confirm_delete.html',
                  context)


class GenreUpdate(UpdateView):
    model = Book
    fields = '__all__'


class GenreDelete(DeleteView):
    model = Author
    success_url = reverse_lazy('books:books')


class GenreListView(ListView):
    model = Genre
    context_object_name = 'genres'
    template_name = 'genre_list.html'
