from datetime import datetime
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView

from django.db.models import Q, Count

from .models import Attendance, Entry
from profiles.models import Student
from .forms import AttendanceForm, EntryForm
from profiles.classes import get_class
from promotion.views import get_random_ads


class IndexPageView(TemplateView):
    template_name = 'index.html'


class ClassesView(LoginRequiredMixin, TemplateView):
    template_name = 'attendance/classes.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Show all active attendance all classes
        active_bca = Attendance.objects.filter(
            Q(class_name__contains='BCA') & Q(is_active=True)).order_by('class_name')
        active_bsc = Attendance.objects.filter(
            Q(class_name__contains='BSC') & Q(is_active=True)).order_by('class_name')
        active_msc = Attendance.objects.filter(
            Q(class_name__contains='MSC') & Q(is_active=True)).order_by('class_name')

        context['active_bca'] = active_bca
        context['active_bsc'] = active_bsc
        context['active_msc'] = active_msc

        return context


class AttendanceListView(LoginRequiredMixin, ListView):
    model = Attendance
    template_name = 'attendance/attendances.html'
    context_object_name = 'attendance_list'
    paginate_by = 50

    def querystring(self):
        qs = self.request.GET.copy()
        qs.pop(self.page_kwarg, None)
        return qs.urlencode()

    def get_queryset(self):
        # Search attendance
        search_txt = self.request.GET.get('q', '')

        # Get selected month name
        current_month = self.request.GET.get('month', datetime.today().month)

        if search_txt:
            qs = Attendance.objects.filter(
                Q(subject_name__icontains=search_txt) |
                Q(teacher__name__icontains=search_txt)).distinct()
        else:
            qs = Attendance.objects.filter(
                att_date__month=current_month)

        return qs.order_by('-att_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        query = self.querystring()
        context['query'] = query

        # Show total classes taken on selected month
        current_month = self.request.GET.get('month', datetime.today().month)

        total_attend = Attendance.objects.filter(
            att_date__month=current_month).values(
                'class_name').annotate(total_class=Count('id'))

        context['total_attend'] = total_attend
        return context


class AttendanceDetailView(LoginRequiredMixin, DetailView):
    model = Attendance
    template_name = 'attendance/attendances_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Get all students from entry table
        entries = Entry.objects.filter(
            Q(attendance=self.kwargs.get('pk'))).order_by('-id')
        total_count = len(entries)

        context['entries'] = entries
        context['total_count'] = total_count
        return context


class AttendanceCreateView(LoginRequiredMixin, CreateView):
    model = Attendance
    template_name = 'attendance/attendances_new.html'
    form_class = AttendanceForm

    def get_initial(self):
        initial = super().get_initial()
        tmp_class = self.request.GET.get('class', '')
        initial['class_name'] = get_class(tmp_class)
        return initial

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        tmp_class = self.request.GET.get('class', '')
        kwargs['active_class'] = get_class(tmp_class)
        return kwargs


class EntryCreateView(CreateView):
    model = Entry
    template_name = 'attendance/entry_new.html'
    form_class = EntryForm

    def get_initial(self):
        initial = super().get_initial()

        # Get class name of current attendance
        self.tmp_class = self.request.GET.get('class', '')
        self.tmp_class = get_class(self.tmp_class)

        # Check if current class attendance is active
        try:
            self.att_obj = Attendance.objects.get(
                class_name=self.tmp_class, is_active=True)
        except Attendance.DoesNotExist:
            self.att_obj = None
        return initial

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()

        kwargs['active_class'] = self.tmp_class
        kwargs['att_obj'] = self.att_obj

        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.att_obj:
            context['attendance'] = self.att_obj
        else:
            context['ads'] = get_random_ads()
            context['not_active'] = 'Attendance is not started by the teacher.'

        return context


class SuccessPageView(TemplateView):
    template_name = 'attendance/success.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['ads'] = get_random_ads()
        return context


class AttendanceReport(LoginRequiredMixin, TemplateView):
    template_name = 'attendance/report.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        tmp_class = self.kwargs.get('class')
        current_month = self.request.GET.get(
            'month', datetime.today().month)

        if get_class(tmp_class) == 'NO_CLASS':
            tmp_class = ''

        # if no class is selected, then show empty list
        if not tmp_class:
            return context

        attendance_list = (
            Attendance.objects.prefetch_related('entry_set__student')
            .filter(class_name=tmp_class, att_date__month=current_month)
            .order_by('att_date')
        )
        total_attendance = attendance_list.count()

        # Get all students from selected class
        all_students = (
            Student.objects.filter(class_name=tmp_class)
            .order_by('name')
        )

        # Convert to list
        all_students = [(student.name, student.pk) for student in all_students]

        # Create attendance dictionary
        report_dict = {}
        for student, s_id in all_students:
            report_dict[student] = [
                s_id, '0%', total_attendance, 0] + ["A"] * total_attendance

        # if there is no attendance, then return student name
        if not attendance_list:
            context['report_dict'] = report_dict
            return context

        report_data = [
            # Initial values for each student
            [s_id, 0, total_attendance, 0] + ["A"] * total_attendance
            for _, s_id in all_students
        ]

        for i, attendance in enumerate(attendance_list):
            present_students = attendance.entry_set.values_list(
                'student__name', flat=True)

            for j, name in enumerate(all_students):
                report_data[j][4 +
                               i] = "P" if name in present_students else "A"

        for student_data in report_data:
            present_count = student_data.count("P")
            student_data[3] = present_count
            student_data[1] = str(
                round((present_count / total_attendance) * 100, 2)) + '%'

        for i, (student, s_id) in enumerate(all_students):
            report_dict[student] = report_data[i]

        context['attendance_list'] = attendance_list
        context['report_dict'] = report_dict

        return context


def end_attendance(request):
    '''End Attendance'''
    if request.method == 'GET':
        att_id = request.GET.get('att_id', '')

        # End Attendance
        try:
            att_obj = get_object_or_404(Attendance, id=att_id)
            att_obj.is_active = False
            att_obj.save()
            result = "success"
        except Attendance.DoesNotExist:
            result = "error"

    return JsonResponse({'result': result})
