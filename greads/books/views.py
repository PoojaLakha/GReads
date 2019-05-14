from django.contrib.auth.decorators import login_required
from django.views import generic
from django.views.generic.edit import UpdateView, DeleteView, FormView
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


from .models import Book, Author, Genre, UserBook
from .forms import BookForm, AuthorForm, GenreForm, UserBookForm
from .search import BookIndex
from .tasks import update_book_cover_summary


# Create your views here.
def es_search(request):
    template = 'books/book_list.html'
    tagHtml = False

    if request.method == 'POST':
        search_text = request.POST['search_text']
    else:
        search_text = ''

    if len(search_text) > 0:
        tagHtml = True

    s = BookIndex.search().query("match", title=search_text)
    response = s.execute()
    response_dict = response.to_dict()
    hits = response_dict['hits']['hits']
    titles = [hit['_source']['title'] for hit in hits]
    book_id = [hit['_id'] for hit in hits]

    book_list = zip(titles, book_id)
    length = len(titles)

    return render(request, template, {'book_list': book_list,
                                      'length': length,
                                      'tagHtml': tagHtml})


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


def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form_isbn = form.cleaned_data['isbn']
            book = form.save(commit=False)
            book.save()
            form.save_m2m()
            update_book_cover_summary.delay(form_isbn)
            return redirect('home')
    else:
        form = BookForm()

    return render(request, 'books/bookform.html', {'form': form})


class BookUpdate(UpdateView):
    model = Book
    fields = '__all__'
    template_name_suffix = '_update_form'


class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('books:books')


def BookConfirm(request, pk=Book.isbn):
    name = Book.objects.get(isbn=pk)
    isbn = pk
    context = {
        'name': name,
        'isbn': isbn
    }
    return render(request, 'books/book_confirm_delete.html',
                  context)


class BookListView(generic.ListView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'book_list'
    paginate_by = 3
    queryset = Book.objects.all()


class BookDetailView(DetailView):
    model = Book
    context_object_name = 'book'
    pk_url_kwarg = 'pk'
    template_name = 'books/book_detail.html'

    def get_context_data(self, **kwargs):
        context = super(BookDetailView, self).get_context_data(**kwargs)
        context['userbook'] = UserBook.objects.filter(user_book=self.object)
        context['user'] = self.request.user
        return context


def add_author(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            author = form.save()
            author.save()
            return redirect('books:add_book')
    else:
        form = AuthorForm()

    return render(request, 'books/authorform.html', {'form': form})


class AuthorDetailView(DetailView):
    model = Author
    template_name = 'books/author_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


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


def add_genre(request):
    if request.method == "POST":
        form = GenreForm(request.POST)
        if form.is_valid():
            genre = form.save()
            genre.save()
            return redirect('books:add_book')
    else:
        form = GenreForm()

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
