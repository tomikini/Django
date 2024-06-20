from django import forms
from .models import Student, Course, Grade

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'birth_date']

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name']

class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ['student', 'course', 'grade', 'date']
