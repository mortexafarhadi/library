from django.urls import path, include

from author import views

urlpatterns = [
    path('all/', views.all_author, name='author-all'),
    path('all-with-temp/', views.all_author_with_template, name='author-all-with-temp'),
    path('<slug:slug>/', views.author_detail, name='author-detail'),
    path('<int:id>', views.author_detail_by_id, name='author-detail-by-id'),
]
