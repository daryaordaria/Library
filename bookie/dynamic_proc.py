from .models import Genre
from .forms import SearchForm


def genre_type(request):
    genre = Genre.objects.all()
    return{'genres': genre}

def search_form(request): 
    form_search = SearchForm 
    if request.method == 'POST':
        form_search = SearchForm(request.POST)
        if form_search.is_valid():
            form_search.save()
    return{'form_search': form_search}

