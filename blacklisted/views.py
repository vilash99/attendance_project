from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404

from django.contrib.auth.decorators import login_required

from .models import BlackListedStudent
from .forms import BlackListStudentForm
from attendance.models import Entry
from profiles.models import Student


@login_required
def blacklist_add(request, entry_id, std_id, att_id):
    template_name = 'blacklisted/new_blacklist.html'

    if request.method == 'GET':
        student = get_object_or_404(Student, id=std_id)
        form = BlackListStudentForm(initial={'student': student,
                                             'tmp_name': student})
        field = form.fields['student']
        field.widget = field.hidden_widget()

        return render(request, template_name, {'form': form})

    if request.method == 'POST':
        student = get_object_or_404(Student, id=std_id)

        form = BlackListStudentForm(request.POST, initial={'student': student,
                                                           'tmp_name': student})
        field = form.fields['student']
        field.widget = field.hidden_widget()

        if form.is_valid():
            form.save()

            # Delete entry from attendance entry
            entry_obj = Entry.objects.get(id=entry_id)
            entry_obj.delete()

            return HttpResponseRedirect('/attendances/' + str(att_id) + "/")

        return render(request, template_name, {'form': form})


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
