from django.http import HttpResponse
from django.shortcuts import render

from .forms import SearchForm
from .google_books_search import GoogleBooksSearch

googleBooksSearch = GoogleBooksSearch()


def get_all_documents(request):
    form = SearchForm(request.POST or None)
    if request.method == 'POST':
        return _get_fields_from_form(request, form)
    return render(request, 'google_books/index.html', {'form': form})


def _get_fields_from_form(request, form):
    keyword = "None"
    if form.is_valid():
        keyword = form.cleaned_data.get("search")
    books_result = googleBooksSearch.search(keyword)
    if len(books_result) == 0:
        return HttpResponse("No books found", status=404)
    else:
        return render(request, 'google_books/show-documents.html', {'books': books_result})
