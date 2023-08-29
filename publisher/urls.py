from django.urls import path

from publisher import views

urlpatterns = [
    path('all/', views.all_publishers, name='all_publishers'),
    path('<slug:slug>/', views.publisher_details, name='publisher-details')
]
