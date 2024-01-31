from django import forms
from .models import BlackListedStudent


class BlackListStudentForm(forms.ModelForm):
    tmp_name = forms.CharField(disabled=True, label='Student name')

    class Meta:
        model = BlackListedStudent
        fields = ['tmp_name', 'student', 'teacher', 'reason']
