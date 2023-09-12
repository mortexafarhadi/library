from django.http import HttpResponse
from django.shortcuts import render

from author.models import Author
from book.models import Book
from site_setting.models import HeaderLink


def all_author(request):
    authors = Author.objects.all()

    context = {
        'authors': authors
    }
    return render(request, 'author/all-author.html', context)


def all_author_with_template(request):
    authors = Author.objects.all()

    header_links = HeaderLink.objects.all()
    context = {
        'title': "Authors",
        'authors': authors,
        "header_links": header_links,
        'footer_description': "salam maryam"
        # 'objects': authors
    }
    return render(request, 'author/all-author-with-temp.html', context)


def author_detail(request, slug):
    author = Author.objects.get(slug=slug)
    context = {
        'author': author,
    }
    return render(request, 'author/detail.html', context)


def author_detail_with_template(request, slug):
    author = Author.objects.get(slug=slug)
    books_author = Book.objects.filter(author=author)
    context = {
        'title': "Author Detail",
        'author': author,
        'books_author': books_author
    }
    return render(request, 'author/single-author-with-temp.html', context)


def author_detail_by_id(request, id):
    author = Author.objects.get(id=id)
    context = {
        'author': author
    }
    return render(request, 'author/detail.html', context)
