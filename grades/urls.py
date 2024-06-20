from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    # Student URLs
    path('students/', views.student_list, name='student_list'),
    path('students/create/', views.student_create, name='student_create'),
    path('students/<int:pk>/edit/', views.student_update, name='student_update'),
    path('students/<int:pk>/delete/', views.student_delete, name='student_delete'),

    # Course URLs
    path('courses/', views.course_list, name='course_list'),
    path('courses/create/', views.course_create, name='course_create'),
    path('courses/<int:pk>/edit/', views.course_update, name='course_update'),
    path('courses/<int:pk>/delete/', views.course_delete, name='course_delete'),

    # Grade URLs
    path('grades/', views.grade_list, name='grade_list'),
    path('grades/create/', views.grade_create, name='grade_create'),
    path('grades/<int:pk>/edit/', views.grade_update, name='grade_update'),
    path('grades/<int:pk>/delete/', views.grade_delete, name='grade_delete'),

    # Report URLs
    path('reports/best_student/', views.report_best_student, name='report_best_student'),
    path('reports/worst_student/', views.report_worst_student, name='report_worst_student'),
    path('reports/average_grades/', views.report_average_grades, name='report_average_grades'),
]
