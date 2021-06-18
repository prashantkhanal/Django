from django.contrib import admin
from Student.models import Student_name
# Register your models here.
@admin.register(Student_name)

class St(admin.ModelAdmin):
    list_display = ['Name', 'Contact', 'Address', 'Email', 'college']

