"""untitled8 URL Configuration
1
1The `urlpatterns` list routes URLs to views. For more information please see:
    https://doc1s.djangoproject.com/en/2.2/topics/http/urls/
Examples:1
F1unction views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import show_main_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('books.urls')),
    path ('', include('categories.urls')),
    path('', show_main_page),

    ]








