from django.http import JsonResponse

from .models import BlackListedStudent
from attendance.models import Entry


def blacklist_student(request):
    '''Blacklist Student'''

    if request.method == 'GET':
        entry_id = request.GET.get('entry_id')

        # Blacklist Selected Student
        student_obj = None
        try:
            entry_obj = Entry.objects.get(id=entry_id)
            student_obj = entry_obj.student  # Save student object
            entry_obj.delete()
            result = "success"
        except Entry.DoesNotExist:
            result = "error"

        # Add Student in Blacklist List
        if result == "success":
            obj = BlackListedStudent(student=student_obj)
            obj.save()

    return JsonResponse({'result': result})


def remove_blacklist(request):
    '''Remove Blacklisted Student'''

    if request.method == 'GET':
        student_id = request.GET.get('student_id')

        # Remove Selected Student from blacklisted
        try:
            student_obj = BlackListedStudent.objects.get(student=student_id)
            student_obj.delete()
            result = "success"
        except BlackListedStudent.DoesNotExist:
            result = "error"

    return JsonResponse({'result': result})
