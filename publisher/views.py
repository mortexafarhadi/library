from django.shortcuts import render

from publisher.models import Publisher


def all_publisher(request):
    publishers = Publisher.objects.all()
    context = {
        'title': 'Publishers',
        # 'publishers': publishers
        'objects': publishers
    }
    return render(request, 'author/all-author-with-temp.html', context)
