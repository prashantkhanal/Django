from django.contrib import admin
from Books.models import BookList

# Register your models here.
@admin.register(BookList)

class Books(admin.ModelAdmin):
    list_display = ['Name', 'Price', 'author']

    