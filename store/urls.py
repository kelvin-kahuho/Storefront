from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
  path("", views.home, name="home"),

  #path('', include("django.contrib.auth.urls")),
  path("store/", views.store, name="store"),
  path("<int:product_id>", views.product, name ="product"),
  path("cart/", views.cart, name="cart"),
  path("checkout/", views.checkout, name="checkout"),

  path("update_item/", views.updateItem, name="update_item"),
  path("dashboard/", views.dashboard, name="dashboard"),
  path("data/", views.data, name="data"),

  #path("login/", views.login, name="login"),
  #path("logout/", views.logout, name="logout"),
]