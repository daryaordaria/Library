from django.urls import path
from . import views

urlpatterns = [
    path('home_page',views.home_page, name = 'home_page'),
    path('books_collection',views.books_collection, name = 'books_collection'),
    path('genre/<str:slug>',views.genre_details, name = 'genre_details'),
    path('book_file/<str:slug>',views.book_details, name = 'book_details'),
    path('resulted_books',views.search_for_book, name = 'search_form'),
    path('login',views.log_in,name = 'login'),
    path('logout',views.log_out,name ='logout'),
    path('registration',views.registration,name = 'registration')
]