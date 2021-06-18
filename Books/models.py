from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class BookList(models.Model):
    Name = models.CharField(max_length=255)
    Price = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null= True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.Name




