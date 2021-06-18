from django.urls import path
from Student.views import student_views, Student_Regest, Studentreg

app_name = "student"

urlpatterns = [
    path('student/', student_views, name="student"),
    path('studentreg/', Studentreg.as_view(), name="Studentregestration"),
    # path("login/", my_view, name="loginpage")
]

