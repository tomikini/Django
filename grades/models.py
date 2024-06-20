from django.db import models
from datetime import date

class Student(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def average_grade(self):
        grades = self.grades.all()
        if grades:
            return sum(grade.grade for grade in grades) / len(grades)
        return 0.0

class Course(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    @property
    def average_grade(self):
        grades = self.grades.all()
        if grades:
            return sum(grade.grade for grade in grades) / len(grades)
        return 0.0

class Grade(models.Model):
    student = models.ForeignKey(Student, related_name='grades', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, related_name='grades', on_delete=models.CASCADE)
    grade = models.DecimalField(max_digits=4, decimal_places=2)
    date = models.DateField(default=date.today)  # Установите значение по умолчанию

    class Meta:
        unique_together = ('student', 'course')

    def __str__(self):
        return f"{self.student} - {self.course}: {self.grade}"
