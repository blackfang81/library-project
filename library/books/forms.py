from django import forms
from .models import Book

class BookForm(forms.ModelForm):

    class Meta:
        model = Book

        fields = [
            'title',
            'author',
            'date_published',
            'isbn'
        ]

class AuthorForm(forms.ModelForm):

    class Meta:
        model = Author

        fields = '__all__'