from django.shortcuts import render
from django.http import HttpResponse
from .models import Books

# Create your views here.
def index(request):
    return render(request, "books/index.html", {
        "books": Books.objects.all()
    })

def add():
    ...

def search():
    ...