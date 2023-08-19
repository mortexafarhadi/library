from django.urls import path

from publisher import views

urlpatterns = [
    path('all/', views.all_publisher),
]
