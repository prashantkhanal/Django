from django.urls import path
from Books.views import Book, BookReg, Bookregestartion

app_name = "Books"
urlpatterns = [
    path('', Book, name="books"),
    path("bookreg/",Bookregestartion.as_view(),  name= 'Bookregestration'),
    
    

]

