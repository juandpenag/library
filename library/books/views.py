from django.shortcuts import render
from .models import Books, Authors, Publishers
from django.db import IntegrityError, DatabaseError
import re

# Create your views here.
def index(request):

    if request.method == 'GET':
        try:
            parameters = {
                "author": request.GET.get('authorship'),
                "title": request.GET.get('title'),
                "publisher": request.GET.get('publisher'),
                "year": request.GET.get('year'),
                "category": request.GET.get('category'),
                "language": request.GET.get('language')
                }
            context = filter(parameters)
        except Exception as e:
            context = {"error_message": e}

    elif request.method == 'POST':
        try:
            parameters = {
                "author": request.POST.get('authorship'),
                "year": request.POST.get('year'),
                "title": request.POST.get('title'),
                "publisher": request.POST.get('publisher'),
                "category": request.POST.get('category'),
                "language": request.POST.get('language')
            }
            context = add(parameters)
        except Exception as e:
            context = {"error_message": e}

    if len(context) > 1:
        return render(request, "books/index.html", context)
    else:
        return render(request, "books/error.html", context)


def filter(parameters):
    try:
        filtered_books = Books.objects.all()

        if parameters['author']: # Compare this code with publisher
            filtered_books = filtered_books.filter(authorship__name=parameters['author']) 

        if parameters['title']:
            filtered_books = filtered_books.filter(title__regex=parameters['title'])
            
        if parameters['year']:
            filtered_books = filtered_books.filter(year=parameters['year'])

        if parameters['publisher']:
            publisher = Publishers.objects.filter(name=parameters['publisher']).first()
            if publisher:
                filtered_books = filtered_books.filter(publisher=publisher)

        if parameters['category']:
            filtered_books = filtered_books.filter(category=parameters['category'])

        if parameters['language']:
            filtered_books = filtered_books.filter(language=parameters['language'])

    except IntegrityError or DatabaseError as e:
        return {"error_message": e}

    return {
            "books": filtered_books,
            "categories": Books.LCC.choices,
            "languages": Books.Languages.choices,
            "authors_list": Authors.objects.all(),
            "publishers_list": Publishers.objects.all()
        }

def add(parameters): # author_name and publisher_name are in the dict

    if any(value is None for value in parameters.values()):
        return {"error_message": "All parameters are needed. Try again."}

    try:
        authorPOST, created = Authors.objects.get_or_create(name=parameters['author'])
        parameters['author'] = authorPOST

        publisherPOST, created = Publishers.objects.get_or_create(name=parameters['publisher'])
        parameters['publisher'] = publisherPOST

        new_book = Books.objects.create(
            authorship = parameters['author'],
            year = parameters['year'],
            title = parameters['title'],
            publisher = parameters['publisher'],
            category = parameters['category'],
            language = parameters['language']            
        )

        new_book.save()

    except IntegrityError or DatabaseError as e:
        return {"error_message": e}
    
    return {
        "books": Books.objects.all(),
        "categories": Books.LCC.choices,
        "languages": Books.Languages.choices,
        "authors_list": Authors.objects.all(),
        "publishers_list": Publishers.objects.all()
    }
