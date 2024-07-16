from django.shortcuts import render
from django.http import HttpResponse
from .models import Books

# Create your views here.
def index(request):
    return render(request, "books/index.html", {
        "books": Books.objects.all()
    })

def filter(request):
    category = request.GET.get('category')
    language = request.GET.get('language')

    filtered_books = Books.objects.all()

    if category:
        filtered_books = filtered_books.filter(category=category)
    if language:
        filtered_books = filtered_books.filter(language=language)

    return render(request, 'books/index.html', {
        "books": filtered_books
    })

def add(request):
    authorPOST = request.POST.get('authorship')
    titlePOST = request.POST.get('title')
    yearPOST = request.POST.get('year')
    publisherPOST = request.POST.get('publisher')
    categoryPOST = request.POST.get('category')
    languagePOST = request.POST.get('language')

    new_book = Books.objects.create(
        authorship = authorPOST,
        year = yearPOST,
        title = titlePOST,
        publisher = publisherPOST,
        category = categoryPOST,
        language = languagePOST
        
    )

    new_book.save()

    return render(request, "books/index.html", {
        "books": Books.objects.all()
    })
