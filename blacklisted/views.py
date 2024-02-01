from django.urls import reverse
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView

from .models import BlackListedStudent
from .forms import BlackListStudentForm


class BlackListCreateView(LoginRequiredMixin, CreateView):
    model = BlackListedStudent
    template_name = 'blacklisted/new_blacklist.html'
    form_class = BlackListStudentForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()

        entry_id = self.kwargs.get('entry_id', None)
        std_id = self.kwargs.get('std_id', None)

        kwargs['entry_id'] = entry_id
        kwargs['std_id'] = std_id

        return kwargs

    def get_success_url(self):
        att_id = self.kwargs.get('att_id', None)
        return reverse('attendance:attendances_detail', args=[str(att_id)])


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
