from django.urls import path

from .views import (IndexPageView, ClassesView, AttendanceListView,
                    AttendanceDetailView, AttendanceCreateView,
                    EntryCreateView, SuccessPageView, AttendanceReport, DeleteAttendance,
                    end_attendance)

app_name = 'attendance'

urlpatterns = [
    path('', IndexPageView.as_view(), name='index'),

    path('classes/', ClassesView.as_view(), name='classes'),

    path('attendances/', AttendanceListView.as_view(), name='attendances'),
    path('attendances/<int:pk>/',AttendanceDetailView.as_view(), name='attendances_detail'),
    path('attendances/new/', AttendanceCreateView.as_view(),name='attendances_new'),
    path('attendances/report/', AttendanceReport.as_view(), name='report'),
    path('attendances/report/<str:class>/',AttendanceReport.as_view(), name='report'),
    path('attendances/<int:pk>/delete/', DeleteAttendance.as_view(), name='delete_attendance'),
    path('end_attendance/', end_attendance, name='end_attendance'),

    path('entry/new/', EntryCreateView.as_view(), name='entry_new'),

    path('success/', SuccessPageView.as_view(), name='success'),
]
