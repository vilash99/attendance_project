from django.contrib import admin
from .models import Attendance, Entry


class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('att_date', 'subject_name', 'class_name',
                    'total_students', 'unique_code', 'is_active')


class EntryAdmin(admin.ModelAdmin):
    list_display = ('attendance', 'student')


admin.site.register(Attendance, AttendanceAdmin)
admin.site.register(Entry, EntryAdmin)
