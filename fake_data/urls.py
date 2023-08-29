from django.urls import path
from . import views

urlpatterns = [
    path('author/<int:count>', views.fake_author, name='fake-author'),
    path('publisher/<int:count>', views.fake_publisher, name='fake-publisher'),
    path('category/<int:count>', views.fake_category, name='fake-category'),
    path('book/<int:count>', views.fake_book, name='fake-book'),
]
