from django.urls import  path

from . import views

urlpatterns = [
    path('categories/', views.show_categories),
    path('categories/<int :categories_id>/',
         views.show_categorw_detail),
]