from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("Books.urls", namespace="Books")),
    path('', include("Student.urls", namespace="student")),
#     path('', include("Teacher.urls", namespace="Teacher"))
    path('', include("Userprofile.urls", namespace="user")),

    
    
# 
]
