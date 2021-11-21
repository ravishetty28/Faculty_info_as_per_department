from django import forms
from django.forms.models import ModelForm
from .models import Faculty, Department

class FacultyForms(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = '__all__'


class DepartmentForms(forms.ModelForm):
    
    class Meta:
        model = Department
        fields = '__all__'

