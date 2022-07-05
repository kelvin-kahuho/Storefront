from django.urls import path
from .templates.hello import views

#URL configuration
urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.greet, name="greet")
]