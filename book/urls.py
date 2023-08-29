from django.urls import path, include
from book import views

urlpatterns = [
    path('all/', views.all_book, name='all_book'),
    path('detail/', views.book_detail, name='book_detail')
]
