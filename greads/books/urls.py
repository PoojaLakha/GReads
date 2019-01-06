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
    path('book/create/', views.BookCreate.as_view(), name='book_create'),
    path('book/<int:pk>/update/', views.BookUpdate.as_view(),
         name='book_update'),
    path('book/<int:pk>/confirm/', views.BookConfirm,
         name='book_delete_confirm'),
    path('book/<int:pk>/delete/', views.BookDelete.as_view(),
         name='book_delete'),
]

'''
urlpatterns += [
    path('author/add/', views.AuthorAdd.as_view(),
            name='author_add'),
    path('author/<int:pk>/update/', views.AuthorUpdate.as_view(),
         name='author_update'),
    path('author/<int:pk>/delete/', views.AuthorDelete.as_view(),
         name='author_delete'),
]
'''