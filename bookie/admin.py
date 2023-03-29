from django.contrib import admin
from .models import Genre, Book, Search

class GenreAdmin(admin.ModelAdmin):
     prepopulated_fields= {'slug': ('name',)}


class BookAdmin(admin.ModelAdmin):
     prepopulated_field = {'slug': ('title',)}


admin.site.register(Genre,GenreAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Search)
