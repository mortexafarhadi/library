from django.shortcuts import render

from book.models import Book


# Create your views here.
def all_book(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'book/all-book.html', context)


def book_detail(request, slug):
    book = Book.objects.get(slug=slug)
    context = {'book': book, }
    return render(request, 'book/single-book.html', context)
