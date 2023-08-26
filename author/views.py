from django.http import HttpResponse
from django.shortcuts import render

from author.models import Author


def all_author(request):
    authors = Author.objects.all()
    context = {
        'authors': authors
    }
    return render(request, 'author/all-author.html', context)


def all_author_with_template(request):
    authors = Author.objects.all()
    context = {
        'title': "Authors",
        'authors': authors,
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
    context = {
        'author': author,
    }
    return render(request, 'author/single-author-with-temp.html', context)


def author_detail_by_id(request, id):
    author = Author.objects.get(id=id)
    context = {
        'author': author
    }
    return render(request, 'author/detail.html', context)
