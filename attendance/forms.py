import random
from django import forms

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
    total_students = forms.IntegerField(
        initial=0,
        widget=forms.NumberInput(attrs={'min': '0', 'max': '300'})
    )

    class Meta:
        model = Attendance
        fields = ['class_name', 'teacher', 'subject_name', 'time_slot', 'total_students']

    def __init__(self, active_class, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['subject_name'].choices = get_subjects(active_class)

    def generate_unique_code(self):
        """Generate a unique code."""
        unique_code = random.randint(100, 10000)
        return unique_code


    def clean(self):
        cleaned_data = super().clean()
        class_name = cleaned_data.get('class_name')
        teacher = cleaned_data.get('teacher')
        subject_name = cleaned_data.get('subject_name')
        time_slot = cleaned_data.get('time_slot')
        time_slots = cleaned_data.get('time_slot')
        attendance_date = self.instance.att_date

        # Validate active attendance for the same class
        if Attendance.objects.filter(class_name=class_name, is_active=True).exists():
            raise forms.ValidationError('Attendance for this class is already ACTIVE!')

        # Ensure only one teacher for theory classes
        if teacher.count() > 1 and not any(keyword in subject_name for keyword in ['Practical', 'VSC:', 'SEC:']):
            raise forms.ValidationError('Theory classes should not have more than one teacher. Are you taking Practical?')

        # Ensure appropriate number of time slots
        if time_slot.count() > 1 and not any(keyword in subject_name for keyword in ['Practical', 'VSC:', 'SEC:']):
            raise forms.ValidationError('Theory classes should have only one time slot. Are you taking Practical?')

        # Ensure practical class have more than one time slot
        if time_slot.count() == 1 and any(keyword in subject_name for keyword in ['Practical', 'VSC:', 'SEC:']):
            raise forms.ValidationError('Practical classes should have more than one time slot. Are you taking Theory?')

        # Check if any of the selected time slots are already used for the same class and date
        for time_slot in time_slots:
            if Attendance.objects.filter(class_name=class_name, time_slot=time_slot, att_date=attendance_date).exists():
                raise forms.ValidationError('Time slot {} has already been used today.'.format(time_slot))

        return cleaned_data

    def save(self, commit=True):
        # Assign a unique code before saving the instance
        self.instance.unique_code = self.generate_unique_code()
        return super().save(commit=commit)



# class EntryForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput())
#     unique_code = forms.IntegerField(initial=0)

#     class Meta:
#         model = Entry
#         fields = ['student', 'password', 'unique_code']

#     def __init__(self, active_class, att_obj, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.active_class = active_class
#         self.att_obj = att_obj
#         self.fields['student'].queryset = Student.objects.filter(class_name=active_class).order_by('name')

#     def clean(self):
#         cleaned_data = super().clean()

#         student = cleaned_data.get('student')
#         password = cleaned_data.get('password')
#         unique_code = cleaned_data.get('unique_code')

#         # Validate password
#         if password == 'abc123':
#             raise forms.ValidationError('Default password is not allowed! Please change your password.')

#         # Check if the password matches the student's password
#         if not Student.objects.filter(class_name=self.active_class, name=student, password=password).exists():
#             raise forms.ValidationError('Incorrect password! Please try again.')

#         # Ensure the student has not already marked attendance
#         if Entry.objects.filter(attendance=self.att_obj, student=student).exists():
#             raise forms.ValidationError('You have already marked attendance for this subject!')

#         # Validate unique code
#         if self.att_obj.unique_code != unique_code:
#             raise forms.ValidationError('Incorrect unique code!')

#         # Ensure not exceeding total students
#         total_present = Entry.objects.filter(attendance=self.att_obj).count()
#         if total_present >= self.att_obj.total_students:
#             raise forms.ValidationError('Your attendance is not saved. Because all students have given attendance. Ask the teacher to resolve this issue.')

#          # Check if the student is blacklisted
#         if BlackListedStudent.objects.filter(student=student).exists():
#             raise forms.ValidationError('You are BLACKLISTED and cannot mark attendance.')

#         return cleaned_data

#     def save(self, commit=True):
#         instance = super().save(commit=False)
#         instance.attendance = self.att_obj
#         if commit:
#             instance.save()
#         return instance
