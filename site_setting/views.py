from django.shortcuts import render

from site_setting.models import HeaderLink


def index(request):
    header_links = HeaderLink.objects.filter(is_active=True)
    context = {
        "header_links": header_links
    }
    return render(request, 'site_setting/index.html', context)





















def header_links_component(request):
    header_links = HeaderLink.objects.filter(is_active=True)
    context = {
        "header_links": header_links
    }
    return render(request, 'site_setting/header_component.html', context)
