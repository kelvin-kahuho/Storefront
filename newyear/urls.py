from django.urls import path
from . import views

#URL configuration
urlpatterns = [
    path("", views.index, name="index"),
]