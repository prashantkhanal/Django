from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect 
from Student.form import StudentRegestration
from django.views.generic import CreateView
from Student.models import Student_name
from django.contrib.auth import authenticate, login
# Create your views here.
def student_views(request):
    return render(request, "inde.html")



def Student_Regest(request):
    if request.method == "POST":
        fm = StudentRegestration(request.POST)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect(reverse('student:student'))
            


    else:
        fm = StudentRegestration()

    return render(request, "form.html", {"form": fm})

""" This is the class based views
"""

class Studentreg(CreateView):
    model = Student_name
    form_class = StudentRegestration
    template_name = "form.html"

    # def get_success_url(self):
    #     return reverse("student:student")



# def my_view(request):
#     username = request.POST.get('prashant')
#     password = request.POST.get('khanal')
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#         login(request, user)
#         return HttpResponseRedirect(reverse("student:loginpage"))
        
#     else:
#         # Return an 'invalid login' error message.
#         return HttpResponseRedirect(reverse("student:student"))
        