from django import forms
from django.db.models import Q

from .models import Attendance, Entry, TimeSlot
from profiles.models import Teacher, Student
from blacklisted.models import BlackListedStudent
from profiles.classes import CLASS_NAMES, get_subjects


class AttendanceForm(forms.ModelForm):
    class_name = forms.ChoiceField(choices=CLASS_NAMES, disabled=True)
    teacher = forms.ModelMultipleChoiceField(
        queryset=Teacher.objects.all().order_by('id'), label='Teachers name')
    subject_name = forms.ChoiceField(choices=[])
    time_slot = forms.ModelMultipleChoiceField(
        queryset=TimeSlot.objects.all().order_by('id'), label='Time slot')
    total_students = forms.IntegerField(initial=0)
    unique_code = forms.IntegerField(initial=0)

    class Meta:
        model = Attendance
        fields = ['class_name', 'teacher', 'subject_name',
                  'time_slot', 'total_students', 'unique_code']

    def __init__(self, active_class, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['subject_name'].choices = get_subjects(active_class)

    def clean(self):
        cleaned_data = super().clean()

        # Check if unique code is used earlier
        clean_unique = cleaned_data.get('unique_code')
        if Attendance.objects.filter(unique_code=clean_unique).exists():
            raise forms.ValidationError('The unique code is used earlier!')

        # Check if same class attendance is active
        clean_class = cleaned_data.get('class_name')
        if Attendance.objects.filter(
                class_name=clean_class, is_active=True).exists():
            raise forms.ValidationError(
                'The attendance for this class is already ACTIVE!')

        teachers = cleaned_data.get('teacher')
        subject_name = cleaned_data.get('subject_name')

        if teachers.count() > 1 and 'Practical' not in subject_name:
             raise forms.ValidationError(
                'Theory class should not have more than one teacher. Are you taking Practical?')

        time_slots = cleaned_data.get('time_slot')
        if time_slots.count() > 1 and 'Practical' not in subject_name:
            raise forms.ValidationError(
                'Theory class should only have one time slot. Are you taking Practical?')

        if time_slots.count() == 1 and 'Practical' in subject_name:
            raise forms.ValidationError(
                'Practical class should have more than one time slots. Are you taking Theory?')

        return cleaned_data


class EntryForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    unique_code = forms.IntegerField(initial=0)

    class Meta:
        model = Entry
        fields = ['student', 'password', 'unique_code']

    def __init__(self, active_class, att_obj, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.active_class = active_class
        self.att_obj = att_obj

        self.fields['student'].queryset = Student.objects.filter(
            class_name=active_class).order_by('name')

    def clean(self):
        cleaned_data = super().clean()

        clean_student = cleaned_data.get('student')
        clean_password = cleaned_data.get('password')
        clean_unique = cleaned_data.get('unique_code')

        # Check if default password abc123 is provided
        if clean_password == 'abc123':
            raise forms.ValidationError(
                'You have entered default password! Please change your password and try again.')

        # Check if student password is correct
        if not Student.objects.filter(class_name=self.active_class,
                                      name=clean_student, password=clean_password).exists():
            raise forms.ValidationError(
                'You have entered wrong password! Please try again.')

        # Check if same student is marking attendance again
        if Entry.objects.filter(attendance=self.att_obj, student=clean_student).exists():
            raise forms.ValidationError(
                'You have already marked your attendance for this subject!')

        # Check if Unique Code is match for given attendance
        if self.att_obj.unique_code != clean_unique:
            raise forms.ValidationError(
                'You have entered wrong Unique Code!')

        # Check if all students have given attendance
        total_present = Entry.objects.filter(
            Q(attendance=self.att_obj.id)).count()

        if total_present >= self.att_obj.total_students:
            raise forms.ValidationError(
                'Your attendance is not saved. Because all students have given attendance. Ask the teacher to resolve this issue.')

        # Check is current student is blacklisted
        if BlackListedStudent.objects.filter(student=clean_student).exists():
            raise forms.ValidationError(
                'You have been BLACKLISTED and are unable to give attendance in any subject.')

        return cleaned_data

    def save(self, commit=True):
        instance = forms.ModelForm.save(self, False)
        instance.attendance = self.att_obj
        instance.save()
        return instance
