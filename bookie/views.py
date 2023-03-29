from django.shortcuts import render, redirect
from .models import Book, Genre
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def books_collection(request):
    books = Book.objects.all()
    return render(request,'books_collection.html',{'books':books})

def home_page(request):
    best_books = Book.objects.filter(best_books=True)
    harry_potter_books = Book.objects.filter(harry_potter_books=True)
    fantastic_beats_books = Book.objects.filter(fantastic_beats_books=True)
    return render(request,'home_page.html',{'best_books':best_books, 'harry_potter_books': harry_potter_books, 
    'fantastic_beats_books':fantastic_beats_books})

def registration(request):
    register = CreateUserForm()
    if request.method == 'POST':
        register = CreateUserForm(request.POST)
        if register.is_valid():
            register.save()
            messages.info(request, "You're registered succesfully!")
            return redirect('login')
    return render(request, 'registration.html',{'register':register})

def log_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('home_page')
        else:
            messages.info(request, "Invalid Credentials")
        
    
    return render(request, 'login.html', {}) 

def log_out(request):
    logout(request)
    return redirect('home_page')


def search_for_book(request):
    resulted_books = Book.objects.filter(title__icontains = request.POST.get('name_book'))
    return render(request, 'search_for_book.html',{'resulted_books': resulted_books})

@login_required(login_url='login')
def book_details(request,slug):
    book = Book.objects.get(slug = slug)
    book_category = book.genre.first()
    book_selection = Book.objects.filter(genre__name__startswith = book_category)
    return render(request, 'book_details.html',{'book': book, 'book_selection': book_selection})

def genre_details(request,slug):
    genre = Genre.objects.get(slug=slug)
    return render(request, 'genre_details.html',{'genre':genre})