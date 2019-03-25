from django.conf.urls import url
# from django.views.generic.base import TemplateView
from . import views

app_name = 'books'

urlpatterns = [
    url(r'^book/$', views.BookListView.as_view(), name='books'),
    url(r'^book/<int:pk>', views.BookDetailView.as_view(),
        name='book-detail'),
    url(r'^search/$', views.es_search, name='esearch'),
    url(r'^book/results/$', views.search, name='search'),
    url(r'^genres/$', views.GenreListView.as_view(), name='genres'),
    url(r'^genres/results/$', views.genresearch, name='gsearch'),
]

urlpatterns += [
    url('book/create/', views.add_book, name='add_book'),
    url('book/<int:pk>/update/', views.BookUpdate.as_view(),
        name='book_update'),
    url('book/<int:pk>/confirm/', views.BookConfirm,
        name='book_delete_confirm'),
    url('book/<int:pk>/delete/', views.BookDelete.as_view(),
        name='book_delete'),
]

urlpatterns += [
    url('author/add/', views.new_author, name='author_add'),
    url('author/<int:pk>/update/', views.AuthorUpdate.as_view(),
        name='author_update'),
    url('author/<int:pk>/confirm/', views.AuthorConfirm,
        name='author_delete_confirm'),
    url('author/<int:pk>/delete/', views.AuthorDelete.as_view(),
        name='author_delete'),
]

urlpatterns += [
    url('genre/add/', views.new_genre, name='genre_add'),
    url('genre/<int:pk>/update/', views.GenreUpdate.as_view(),
        name='genre_update'),
    url('genre/<int:pk>/confirm/', views.GenreConfirm,
        name='genre_delete_confirm'),
    url('genre/<int:pk>/delete/', views.GenreDelete.as_view(),
        name='genre_delete'),
]
