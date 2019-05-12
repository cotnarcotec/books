from django.shortcuts import HttpResponse

from categories.models import Category


def show_categoris(request):
    categories = Category.obgects.all()
    result = ''

    for categories in categories:
        result += f'<a href="(category.id)">'\

    return HttpResponse(result)

def show_category_detail(request, category_id):
    category = Category.objects.get(id=category_id)
    result = f'(category.neme)'
    books = category.books.all()
    return HttpResponse(result)
