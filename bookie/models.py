from django.db import models

# Create your models here.


class Genre(models.Model):
    name = models.CharField('Genres', max_length = 25)
    slug = models.SlugField(max_length = 40)
    def __str__(self):
        return self.name

class Search(models.Model):
      name_book = models.CharField(max_length= 50)
      def __str__(self):
          return self.name_book


class Book(models.Model):
    title = models.CharField(max_length = 100)
    slug = models.SlugField(max_length=100)
    book_cover = models.ImageField(upload_to = 'img', blank = True, null= True)
    author_name = models.CharField(max_length = 100)
    description = models.TextField()
    genre = models.ManyToManyField(Genre, related_name = 'books')
    book_file = models.FileField(upload_to='book_file')
    best_books = models.BooleanField(default=False)
    harry_potter_books = models.BooleanField(default=False)
    fantastic_beats_books = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title