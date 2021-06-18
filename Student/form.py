from django import forms
from Student.models import Student_name

class StudentRegestration(forms.ModelForm):
    class Meta:
        model = Student_name
        exclude = ['modified', 'created']

        
