from django.urls import path, include
from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework import routers
from django.conf.urls.static import static
from django.conf import settings

router = routers.DefaultRouter()

from . import views

urlpatterns = [
  path("", views.home, name="home"),

  #path('', include("django.contrib.auth.urls")),
  path("store/", views.store, name="store"),
  path("<int:product_id>", views.product, name ="product"),
  path("cart/", views.cart, name="cart"),
  path("checkout/", views.checkout, name="checkout"),
  path('api/', include(router.urls)),
  path("update_item/", views.updateItem, name="update_item"),
  path("dashboard/", views.dashboard, name="dashboard"),
  path("product_rating/", views.product_rating, name="rating"),
  path("send_data/", views.send_data, name="data"),
  path("signup/", views.signupUser, name="signup"),
  path("login/", views.loginUser, name="login"),
  path("logout/", views.logoutUser, name="logout"),
]

