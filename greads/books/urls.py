from django.urls import path
# from django.views.generic.base import TemplateView
from . import views

app_name = 'books'

urlpatterns = [
    path('', views.index, name='index'),
    path('book/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
]

urlpatterns += [
    path('book/create/', views.new_book, name='book_add'),
    path('book/<int:pk>/update/', views.BookUpdate.as_view(),
         name='book_update'),
    path('book/<int:pk>/confirm/', views.BookConfirm,
         name='book_delete_confirm'),
    path('book/<int:pk>/delete/', views.BookDelete.as_view(),
         name='book_delete'),
]

urlpatterns += [
    path('author/add/', views.new_author, name='author_add'),
    path('author/<int:pk>/update/', views.AuthorUpdate.as_view(),
         name='author_update'),
    path('author/<int:pk>/confirm/', views.AuthorConfirm,
         name='author_delete_confirm'),
    path('author/<int:pk>/delete/', views.AuthorDelete.as_view(),
         name='author_delete'),
]

urlpatterns += [
    path('genre/add/', views.new_genre, name='genre_add'),
    path('genre/<int:pk>/update/', views.GenreUpdate.as_view(),
         name='genre_update'),
    path('genre/<int:pk>/confirm/', views.GenreConfirm,
         name='genre_delete_confirm'),
    path('genre/<int:pk>/delete/', views.GenreDelete.as_view(),
         name='genre_delete'),
]
