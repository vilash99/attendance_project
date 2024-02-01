from datetime import datetime
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView

from django.db.models import Q

from .models import Teacher, Student
from attendance.models import Attendance, Entry
from blacklisted.models import BlackListedStudent


class TeacherListView(LoginRequiredMixin, ListView):
    model = Teacher
    template_name = 'profiles/teacher.html'
    context_object_name = 'teacher_list'


class TeacherDetailView(LoginRequiredMixin, DetailView):
    model = Teacher
    template_name = 'profiles/teacher_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Get selected month name
        current_month = self.request.GET.get('month', datetime.today().month)

        attendance_list = Attendance.objects.filter(Q(teacher=self.kwargs.get(
            'pk')) & Q(att_date__month=current_month)).order_by('att_date')
        context['attendance_list'] = attendance_list

        # Get total theory and practical classes
        total_theory = Attendance.objects.filter(Q(teacher=self.kwargs.get('pk')) & Q(
            att_date__month=current_month) & ~Q(subject_name__contains="Practical")).count()
        total_practical = Attendance.objects.filter(Q(teacher=self.kwargs.get('pk')) & Q(
            att_date__month=current_month) & Q(subject_name__contains="Practical")).count()

        context['total_theory'] = total_theory
        context['total_practical'] = total_practical

        return context


class TeacherCreateView(LoginRequiredMixin, CreateView):
    model = Teacher
    template_name = 'profiles/teacher_new.html'
    fields = '__all__'


class TeacherUpdateView(LoginRequiredMixin, UpdateView):
    model = Teacher
    template_name = 'profiles/teacher_edit.html'
    fields = ['name']


class StudentListView(LoginRequiredMixin, ListView):
    model = Student
    template_name = 'profiles/student.html'
    context_object_name = 'student_list'
    paginate_by = 50

    def querystring(self):
        qs = self.request.GET.copy()
        qs.pop(self.page_kwarg, None)
        return qs.urlencode()

    def get_queryset(self):
        # Search student
        search_txt = self.request.GET.get('q', '')
        qs = Student.objects.filter(name__icontains=search_txt)
        return qs.order_by('name')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        query = self.querystring()
        context['query'] = query

        return context


class StudentDetailView(LoginRequiredMixin, DetailView):
    model = Student
    template_name = 'profiles/student_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Get selected month name
        current_month = self.request.GET.get('month', datetime.today().month)

        tmp_student = Student.objects.get(pk=self.kwargs.get('pk'))

        # Count total number classes for given student class
        total_classes = Attendance.objects.filter(
            Q(class_name=tmp_student.class_name) & Q(att_date__month=current_month)).count()

        # Total present in given month
        attendance_list = Entry.objects.filter(
            Q(student=self.kwargs.get('pk')) & Q(attendance__att_date__month=current_month))

        total_present = len(attendance_list)
        if total_classes != 0:
            percent = str(round((total_present*100)/total_classes, 2))
        else:
            percent = '0.00'

        # Check if student is blacklisted
        try:
            blacklisted = BlackListedStudent.objects.get(
                student=self.kwargs.get('pk'))
        except:
            blacklisted = None

        context['attendance_list'] = attendance_list
        context['total_classes'] = total_classes
        context['total_present'] = total_present
        context['present_percent'] = percent + '%'
        context['blacklisted'] = blacklisted

        return context


class StudentCreateView(LoginRequiredMixin, CreateView):
    model = Student
    template_name = 'profiles/student_new.html'
    fields = '__all__'


class StudentUpdateView(LoginRequiredMixin, UpdateView):
    model = Student
    template_name = 'profiles/student_edit.html'
    fields = ['name', 'class_name', 'password']


def change_password(request):
    '''Student password changing'''

    if request.method == 'GET':
        status = ''

        student_id = request.GET.get('student_id')
        old_pass = request.GET.get('old_pass')
        new_pass = request.GET.get('new_pass')

        # Check if Student is exit and old password is matched
        try:
            student_obj = Student.objects.get(id=student_id)
            if student_obj.password == old_pass:
                student_obj.password = new_pass
                student_obj.save()

                message_txt = 'Password is changed successfully! Your new password is shown below.'
                status = 'success'
            else:
                message_txt = 'Entered old password is not matched with existing password!'
                status = 'error'

        except Student.DoesNotExist:
            message_txt = 'Your name is not exists in attendance list.'
            status = 'error'

    return JsonResponse({'message_txt': message_txt, 'status': status})


def error_500(request):
    """
    Show 500 error page
    """
    return render(request, 'exception/error500.html')


def error_404(request, exception):
    """
    Show 404 error page
    """
    return render(request, 'exception/error404.html')


def faq_page(request):
    """
    Show FAQ for password
    """
    return render(request, 'exception/faq_password.html')
