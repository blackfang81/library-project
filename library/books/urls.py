from django.urls import path
from . import views

urlpatterns = [

    path('', views.list_book, name='book_list'),

    path(
        'book/<int:id>/',
        views.detail_book,
        name='book_detail'
    ),

    path(
        'book/add/',
        views.update_create_book,
        name='book_add'
    ),

    path(
        'book/edit/<int:id>/',
        views.update_create_book,
        name='book_edit'
    ),
]