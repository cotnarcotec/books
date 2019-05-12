from django.http import HttpResponse

from books.models import Book


def show_books(request):
    books = Book.objects.all()
    result = ''

    for book in books:
        result += f'{book.neme}<hr>'

    return HttpResponse(result)

def show_book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    result = f'{book.neme}<br>{book.price}'
    return HttpResponse(result)


