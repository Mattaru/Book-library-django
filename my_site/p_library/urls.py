from django.contrib import admin
from django.urls import path

from .views import (
        BookList,
        BookCreate,
        BookUpdate,
        BookDelete,
        book_increment,
        book_decrement,
        AuthorCreate,
        AuthorList,
        AuthorUpdate,
        AuthorDelete,
        author_create_many,
        books_authors_create_many,
        FriendList,
        FriendCreate,
        FriendUpdate,
        FriendDelete,
        PublisherList,
        PublisherCreate,
        PublisherUpdate,
        PublisherDelete,
)


app_name = 'p_library'

urlpatterns = [
        path('book/create/', BookCreate.as_view(), name='book_create'),
        path('book/', BookList.as_view(), name='book_list'),
        path('book/<int:pk>/', BookUpdate.as_view(), name='book_edit'),
        path('book/<int:pk>/delete/', BookDelete.as_view(), name='book_delete'),
        path('book/book_increment/', book_increment),
        path('book/book_decrement/', book_decrement),

        path('author/create/', AuthorCreate.as_view(), name='author_create'),
        path('author/', AuthorList.as_view(), name='author_list'),
        path('author/<int:pk>/', AuthorUpdate.as_view(), name='author_edit'),
        path('author/<int:pk>/delete/', AuthorDelete.as_view(), name='author_delete'),

        path('author/create_many/', author_create_many, name='author_create_many'),
        path('author_book/create_many/', books_authors_create_many, name='author_book_create_many'),

        path('friend/create/', FriendCreate.as_view(), name='friend_create'),
        path('friend/', FriendList.as_view(), name='friend_list'),
        path('friend/<int:pk>/', FriendUpdate.as_view(), name='friend_edit'),
        path('friend/<int:pk>/delete/', FriendDelete.as_view(), name='friend_delete'),

        path('publisher/create/', PublisherCreate.as_view(), name='publisher_create'),
        path('publisher/', PublisherList.as_view(), name='publisher_list'),
        path('publisher/<int:pk>/', PublisherUpdate.as_view(), name='publisher_edit'),
        path('publisher/<int:pk>/delete/', PublisherDelete.as_view(), name='publisher_delete'),
]