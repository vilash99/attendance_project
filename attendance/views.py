from datetime import datetime
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView

from django.db.models import Q, Count

from .models import Attendance, Entry
from profiles.models import Student
from .forms import AttendanceForm
from profiles.classes import get_class, CLASS_NAMES
from promotion.views import get_random_ads


class IndexPageView(TemplateView):
    template_name = 'index.html'


class ClassesView(LoginRequiredMixin, TemplateView):
    template_name = 'attendance/classes.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Filter all active attendance by class name and status
        class_filters = {
            'active_bca': 'BCA',
            'active_bsc': 'BSC',
            'active_msc': 'MSC',
        }

        for key, class_name in class_filters.items():
            context[key] = Attendance.objects.filter(
                class_name__icontains=class_name, is_active=True
            ).order_by('class_name')

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
        """Filters queryset based on search text or selected month."""
        search_txt = self.request.GET.get('q', '')
        current_month = int(self.request.GET.get('month', datetime.today().month))

        queryset = Attendance.objects.all()

        if search_txt:
            queryset = queryset.filter(
                Q(subject_name__icontains=search_txt) |
                Q(teachers__name__icontains=search_txt)
            ).distinct()
        else:
            queryset = queryset.filter(att_date__month=current_month)

        return queryset.order_by('-id', '-att_date')

    def get_context_data(self, **kwargs):
        """Adds additional context including querystring and total attendance per class."""
        context = super().get_context_data(**kwargs)
        query = self.querystring()
        context['query'] = query

        current_month = int(self.request.GET.get('month', datetime.today().month))

        # Annotate total classes taken per class for the selected month
        total_attend = Attendance.objects.filter(
            att_date__month=current_month
        ).values('class_name').annotate(total_class=Count('id'))

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

        context['entries'] = entries
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


class EntryCreateView(TemplateView):
    model = Entry
    template_name = 'attendance/entry_new.html'
    # form_class = EntryForm

    # def get_initial(self):
    #     initial = super().get_initial()

    #     # Get class name of current attendance
    #     self.tmp_class = self.request.GET.get('class', '')
    #     self.tmp_class = get_class(self.tmp_class)

    #     # Check if current class attendance is active
    #     try:
    #         self.att_obj = Attendance.objects.get(
    #             class_name=self.tmp_class, is_active=True)
    #     except Attendance.DoesNotExist:
    #         self.att_obj = None
    #     return initial

    # def get_form_kwargs(self):
    #     kwargs = super().get_form_kwargs()

    #     kwargs['active_class'] = self.tmp_class
    #     kwargs['att_obj'] = self.att_obj

    #     return kwargs

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)

    #     if self.att_obj:
    #         context['attendance'] = self.att_obj
    #     else:
    #         context['ads'] = get_random_ads()
    #         context['not_active'] = 'Attendance is not started by the teacher.'

    #     return context


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

        context['CLASS_NAMES'] = CLASS_NAMES

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

            for j, (name, s_id) in enumerate(all_students):
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


class DeleteAttendance(LoginRequiredMixin, DeleteView):
    model = Attendance
    template_name = 'attendance/confirm_delete_attendance.html'
    success_url = '/attendances/'


class AttendanceCompleteReport(LoginRequiredMixin, TemplateView):
    template_name = 'attendance/complete_attendance_report.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['CLASS_NAMES'] = CLASS_NAMES

        months = [
            {"num": "7", "name": "July"},
            {"num": "8", "name": "August"},
            {"num": "9", "name": "September"},
            {"num": "10", "name": "October"},
            {"num": "11", "name": "November"},
            {"num": "12", "name": "December"},
            {"num": "1", "name": "January"},
            {"num": "2", "name": "February"},
            {"num": "3", "name": "March"},
            {"num": "4", "name": "April"},
            {"num": "5", "name": "May"},
            {"num": "6", "name": "June"},
        ]

        tmp_class = self.kwargs.get('class')

        if not tmp_class:
            return context

        # Get all students of selected class
        students = Student.objects.filter(class_name=tmp_class).order_by('name')
        all_students_attendance = []

        for student in students:
            monthly_attendance = {}

            # Loop through each month from July (7) to June (6)
            for month in range(7, 19):
                tmp_month = (month if month <= 12 else month - 12)

                # Count total classes for the given month and student's class
                total_classes = Attendance.objects.filter(
                    Q(class_name=student.class_name) & Q(att_date__month=tmp_month)
                ).count()

                # If there are no classes in this month, skip to the next month
                if total_classes == 0:
                    continue

                # Total present days in the given month
                total_present = Entry.objects.filter(
                    Q(student=student) & Q(attendance__att_date__month=int(tmp_month))
                ).count()

                percent = round((total_present * 100) / total_classes, 2) if total_classes else 0.0

                # Append the data for the current month
                monthly_attendance[tmp_month] = {
                    # 'total_classes': total_classes,
                    # 'total_present': total_present,
                    'present_percent': f"{percent:.2f}%"
                }

            # Append the student's attendance data to the list
            all_students_attendance.append({
                'student': student,
                'monthly_attendance': monthly_attendance
            })

        # Pass the attendance data for all students to the context
        context['all_students_attendance'] = all_students_attendance
        context['months'] = months
        return context