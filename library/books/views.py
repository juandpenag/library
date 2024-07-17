from django.shortcuts import render
from django.http import HttpResponse
from .models import Books, Authors, Publishers
from django.db import IntegrityError, DatabaseError

# Create your views here.
def index(request):
    try:
        context = {
        "books": Books.objects.all(),
        "categories": Books.LCC.choices,
        "languages": Books.Languages.choices,
        "authors_list": Authors.objects.all(),
        "publishers_list": Publishers.objects.all()    
    }
    except DatabaseError as e:
        return render(request, "books/error.html", {"error_message": e})
    
    return render(request, "books/index.html", context)

def filter(request):
    try:
        authorGET = request.GET.get('authorship')
        titleGET = request.GET.get('title')
        publisherGET = request.GET.get('publisher')
        yearGET = request.GET.get('year')
        categoryGET = request.GET.get('category')
        languageGET = request.GET.get('language')

        filtered_books = Books.objects.all()

        if authorGET:
            filtered_books = filtered_books.filter(authoship=authorGET)
        if titleGET:
            filtered_books = filtered_books.filter(title=titleGET)
        if publisherGET:
            filtered_books = filtered_books.filter(publisher=publisherGET)
        if yearGET:
            filtered_books = filtered_books.filter(year=yearGET)
        if categoryGET:
            filtered_books = filtered_books.filter(category=categoryGET)
        if languageGET:
            filtered_books = filtered_books.filter(language=languageGET)
        
        context = {
        "books": filtered_books,
        "categories": Books.LCC.choices,
        "languages": Books.Languages.choices,
        "authors_list": Authors.objects.all(),
        "publishers_list": Publishers.objects.all()
    }
    except DatabaseError as e:
        return render(request, "books/error.html", {"error_message": e})

    return render(request, 'books/index.html', context)

def add(request):
    if request.method == 'POST':
        author_name = request.POST.get('authorship')
        publisher_name = request.POST.get('publisher')
        titlePOST = request.POST.get('title')
        yearPOST = request.POST.get('year')
        categoryPOST = request.POST.get('category')
        languagePOST = request.POST.get('language')

    if not(author_name and publisher_name and titlePOST and yearPOST and categoryPOST and languagePOST):
        return render(request, "books/error.html", {"error_message": "All fields are required."})

    try: 
        authorPOST, created = Authors.objects.get_or_create(name=author_name)
        publisherPOST, created = Publishers.objects.get_or_create(name=publisher_name)

        new_book = Books.objects.create(
            authorship = authorPOST,
            year = yearPOST,
            title = titlePOST,
            publisher = publisherPOST,
            category = categoryPOST,
            language = languagePOST            
        )
    except IntegrityError as e:
        return render(request, "books/error.html", {"error_message": e})

    new_book.save()

    return render(request, "books/index.html", {
        "books": Books.objects.all(),
        "categories": Books.LCC.choices,
        "languages": Books.Languages.choices,
        "authors_list": Authors.objects.all(),
        "publishers_list": Publishers.objects.all()
    })
