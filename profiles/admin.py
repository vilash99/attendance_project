from django.contrib import admin
from .models import Teacher, Student


class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'class_name')
    search_fields = ["name"]


admin.site.register(Teacher)
admin.site.register(Student, StudentAdmin)
