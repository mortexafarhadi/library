from django.urls import path
from site_setting import views

urlpatterns = [
    path('',views.index, name="index")
]