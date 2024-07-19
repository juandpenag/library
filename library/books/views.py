from django.shortcuts import render
from django.http import HttpResponse
from .models import Books, Authors, Publishers
from django.db import IntegrityError, DatabaseError
import re

# Create your views here.
def index(request):
    try:
        if request.method == 'GET':
            filtered_books = Books.objects.all()
            authorGET = request.GET.get('authorship')
            titleGET = request.GET.get('title')
            publisherGET = request.GET.get('publisher')
            yearGET = request.GET.get('year')
            categoryGET = request.GET.get('category')
            languageGET = request.GET.get('language')

            if authorGET:
                filtered_books = filtered_books.filter(authorship__name=authorGET) 
            if titleGET:
                filtered_books = filtered_books.filter(title__regex=titleGET)
            if publisherGET:
                publisher = Publishers.objects.filter(name=publisherGET).first()
                if publisher:
                    filtered_books = filtered_books.filter(publisher=publisher)
            if yearGET:
                filtered_books = filtered_books.filter(year=yearGET)
            if categoryGET:
                filtered_books = filtered_books.filter(category=categoryGET)
            if languageGET:
                filtered_books = filtered_books.filter(language=languageGET)

            context  = {
                "books": filtered_books,
                "categories": Books.LCC.choices,
                "languages": Books.Languages.choices,
                "authors_list": Authors.objects.all(),
                "publishers_list": Publishers.objects.all()
            }
        elif request.method == 'POST':
            author_name = request.POST.get('authorship')
            publisher_name = request.POST.get('publisher')
            titlePOST = request.POST.get('title')
            yearPOST = request.POST.get('year')
            categoryPOST = request.POST.get('category')
            languagePOST = request.POST.get('language')

            if not(author_name and publisher_name and titlePOST and yearPOST and categoryPOST and languagePOST):
                return render(request, "books/error.html", {"error_message": "Go back and fill them all."})

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

            new_book.save()

            context  = {
                "books": Books.objects.all(),
                "categories": Books.LCC.choices,
                "languages": Books.Languages.choices,
                "authors_list": Authors.objects.all(),
                "publishers_list": Publishers.objects.all()
            }

    except IntegrityError or DatabaseError as e:
        return render(request, "books/error.html", {"error_message": e})

    return render(request, "books/index.html", context)
