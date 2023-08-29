from django.shortcuts import render

from book.models import Book
from publisher.models import Publisher


def all_publishers(request):
    publishers = Publisher.objects.all()
    context = {
        'publishers': publishers
    }
    return render(request, 'publisher/all-publisher.html', context)


def publisher_details(request, slug):
    publisher = Publisher.objects.get(slug=slug)
    publisher_books = Book.objects.filter(publisher=publisher)
    book_categories_list = publisher_books.values('category__title')

    book_categories = []

    for i in book_categories_list:
        if i not in book_categories:
            book_categories.append(i)

    publisher_books = publisher_books[:5]

    context = {
        'publisher': publisher,
        'publisher_books': publisher_books,
        'book_categories': book_categories
    }
    return render(request, 'publisher/publisher-detail.html', context)
