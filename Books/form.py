from django import forms
from Books.models import BookList

class Bookslist(forms.ModelForm):
    class Meta:
        model = BookList
        exclude = ['created', 'modified']


        