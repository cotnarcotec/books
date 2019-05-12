from django.urls import  path

from . import views

urlpatterns = [
    path('books/', views.show_books),
    path('books/<int :books_id>/',
         views.show_book_detail),

]