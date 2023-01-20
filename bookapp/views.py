from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.http import HttpResponse
from .models import *
from .forms import BookForm, BookUpdateForm
# Create your views here.


def index(request):
    return render(request, 'bookapp/bookshop.html')


# View for Add Books
def add_books(request):
    if request.method == "GET":
       form = BookForm()
       context = {'form': form}
       template_name = 'bookapp/addBook.html'
       return render(request, template_name, context)

    if request.method == "POST":
        title = request.POST['title']
        author = request.POST['author']
        publisher = request.POST['publisher']
        language = request.POST['language']
        copies = request.POST['copies']
        book = BookDB(title=title, author=author,
                      publisher=publisher, language=language, copies=copies)
        if book is not None:
            book.save()
            return HttpResponse(' Book Added  Sucessfully!')
            # print(book.title)
        return HttpResponse('Not Added !!!!')


# View for Display books
def view_books(request):
    all_books = BookDB.objects.all()
    cntx = {"books": all_books}
    return render(request, 'bookapp/viewBooks.html', cntx)


def delete_books(request):
    if request.method == "GET":
        return render(request, 'bookapp/delBook.html')
    if request.method == "POST":
        B_id = request.POST['book_id']
        delete_book = BookDB.objects.get(id=B_id)
        if delete_book is not None:
            delete_book.delete()
            return HttpResponse('Book Deleted !!!')
    else:
        return HttpResponse('Book Not Exist !!')

# View For Search Book By ID


def search_book(request):
    if request.method == "GET":
        return render(request, 'bookapp/searchbook.html')
    if request.method == "POST":
        bid = request.POST['book_id']
        book = BookDB.objects.get(id=bid)
        c = {"book": book}
        return render(request, 'bookapp/searchbook.html', c)

# View for Updation


def upd_books(request,id):
    if request.method == "GET": 
        book = BookDB.objects.get(id=id)
        c = {"book":book}
        return render(request,'bookapp/updateBook.html',c)
    if request.method == "POST":
        # bid = request.POST['book_id']
        book = BookDB.objects.get(id=id)
        book.title = request.POST['title']
        book.author = request.POST['author']
        book.publisher = request.POST['publisher']
        book.language = request.POST['language']
        book.copies = request.POST['copies']
        book.save()
        return HttpResponse(' updated !')