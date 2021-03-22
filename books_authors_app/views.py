from django.shortcuts import render,redirect
from .models import Book, Author

def index(request):
    return render(request,"index.html")
