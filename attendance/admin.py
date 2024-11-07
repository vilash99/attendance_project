from django.contrib import admin
from .models import Attendance, Entry, TimeSlot, Token


class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('att_date', 'subject_name', 'class_name',
                    'total_students', 'unique_code', 'is_active')


class EntryAdmin(admin.ModelAdmin):
    list_display = ('attendance', 'student')


class TimeSlotAdmin(admin.ModelAdmin):
    list_display = ('slot',)

class TokenAdmin(admin.ModelAdmin):
    list_display = ('student', 'token', 'created_at')


admin.site.register(Attendance, AttendanceAdmin)
admin.site.register(Entry, EntryAdmin)
admin.site.register(TimeSlot, TimeSlotAdmin)
admin.site.register(Token, TokenAdmin)
