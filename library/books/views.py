from django.shortcuts import render
from .models import Book
from django.shortcuts import get_object_or_404
from .forms import BookForm

def list_book(request):

    books = Book.objects.all()

    return render(
        request,
        'book_list.html',
        {'books': books}
    )

def detail_book(request, id):

    book = get_object_or_404(Book, id=id)

    return render(
        request,
        'book_detail.html',
        {'book': book}
    )

def update_create_book(request, id=None):

    if id:
        book = get_object_or_404(Book, id=id)
    else:
        book = None

    if request.method == 'POST':

        form = BookForm(
            request.POST,
            instance=book
        )

        if form.is_valid():
            form.save()

    else:

        form = BookForm(
            instance=book
        )

    return render(
        request,
        'book_form.html',
        {'form': form}
    )