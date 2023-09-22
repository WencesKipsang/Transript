from django import forms
from . import models

class AddStudent(forms.ModelForm):
    class Meta:
        model=models.Student
        fields ='__all__'
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }
        
class AddSchool(forms.ModelForm):
    class Meta:
       model=models.School
       fields='__all__'
       
class AddDepartment(forms.ModelForm):
    class Meta:
        model=models.Department
        fields='__all__'

class AddCourse(forms.ModelForm):
    class Meta:
        model=models.Course
        fields='__all__'
        
class AddUnit(forms.ModelForm):
    class Meta:
        model=models.Units
        fields='__all__'