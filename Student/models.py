from django.db import models

# Create your models here.


class College_name(models.Model):
    Name = models.CharField(max_length=255)
    Address = models.CharField(max_length=255, null=True, blank=True)
    
    def __str__(self):
        return self.Name

class Student_name(models.Model):
    Name = models.CharField(max_length=255)
    Contact = models.CharField(max_length=255)
    Address = models.CharField(max_length=255)
    Email = models.EmailField(max_length=255)
    college = models.ForeignKey(College_name, on_delete=models.CASCADE, null=True, blank=True)


    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Name

