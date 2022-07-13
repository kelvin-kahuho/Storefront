from django.urls import path

from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
  path("", views.store, name="store"),
  path("cart/", views.cart, name="cart"),
  path("checkout/", views.checkout, name="checkout"),

  path("update_item/", views.checkout, name="update_item"),
  path("dashboard/", views.dashboard, name="dashboard"),
  path("data/", views.data, name="data"),
]