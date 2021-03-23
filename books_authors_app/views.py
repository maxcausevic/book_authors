from django.shortcuts import render,redirect
from .models import Book, Author

def index(request):
    all_books = Book.objects.all()
    context = {
        'all_books' : all_books
        }
    return render(request,"index.html", context)
def authors_index(request):
    all_authors = Author.objects.all()
    context = {
        "all_authors" : all_authors
    }
    return render(request,"create_authors.html", context)
def create_book(request):    
    Book.objects.create(
        title=request.POST['title'],
        description=request.POST["description"]
    )
    return redirect("/")
def create_author(request):
    Author.objects.create(
        name=request.POST['author_name'],
        notes=request.POST['notes'],
    )
    return redirect("/authors")
def display_book(request, book_id):
    correct_book = Book.objects.get(id=book_id)
    context = {
        "correct_book" : correct_book,
        "all_authors" : Author.objects.all()
    }
    return render(request,"display_book.html", context)
def display_author(request, author_id):
    correct_author = Author.objects.get(id=author_id)
    context = {
        "correct_author" : correct_author,
        "all_books" : Book.objects.all()
    }
    return render(request,"display_author.html", context)
def add_author(request):
    this_book = Book.objects.get(id=request.POST['book_id'])
    this_author = Author.objects.get(id=request.POST['author_id'])
    this_book.authors.add(this_author)
    return redirect(f"/display_book/{this_book.id}")
def add_book(request):
    this_book = Book.objects.get(id=request.POST['book_id'])
    this_author = Author.objects.get(id=request.POST['author_id'])
    this_author.books.add(this_book)
    return redirect(f"/display_author/{this_author.id}")
