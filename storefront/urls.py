"""storefront URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import include, path


from django.conf.urls.static import static
from django.conf import settings
#from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('hello/', include("hello.urls")),
    #path('newyear/', include("newyear.urls")),
    #path('tasks/', include("tasks.urls")),
    path('', include("store.urls")),
    path('recommendations/', include("api.urls")),
    #url(r'^oauth2/', include('oauth2_authentication.urls', namespace="oauth2")),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)