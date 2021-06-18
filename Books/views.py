from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from Books.form import Bookslist
from django.views.generic import CreateView
from Books.models import BookList

# Create your views here.

def Book(request):
    return render(request, "index.html")


def BookReg(request):
    if request.method == "POST":
        fm = Bookslist(request.POST)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect(reverse("Books:books"))

    else:
        fm = Bookslist()


    return render(request, "form.html", {"form": fm})


class Bookregestartion(CreateView):
    model = BookList
    form_class = Bookslist
    template_name = "form.html"

    def get_success_url(self):
        return reverse('Books:books')












