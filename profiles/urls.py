from django.urls import path
from .views import (TeacherListView, TeacherDetailView, TeacherCreateView,
                    TeacherUpdateView, StudentListView, StudentDetailView,
                    StudentCreateView, StudentUpdateView, change_password)

app_name = 'profiles'

urlpatterns = [
    path('teacher/', TeacherListView.as_view(), name='teacher'),
    path('teacher/new/', TeacherCreateView.as_view(), name='teacher_new'),
    path('teacher/<int:pk>/',
         TeacherDetailView.as_view(), name='teacher_detail'),
    path('teacher/<int:pk>/edit/',
         TeacherUpdateView.as_view(), name='teacher_edit'),

    path('student/', StudentListView.as_view(), name='student'),
    path('student/new/', StudentCreateView.as_view(), name='student_new'),
    path('student/<int:pk>/',
         StudentDetailView.as_view(), name='student_detail'),
    path('student/<int:pk>/edit/',
         StudentUpdateView.as_view(), name='student_edit'),

    path('change_password/', change_password, name='change_password'),
]
