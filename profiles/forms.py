from django import forms
from .models import Student
from profiles.classes import get_class

class PasswordChangeFromAPIForm(forms.Form):
    student = forms.ModelChoiceField(queryset=Student.objects.none(), label="Student")
    old_password = forms.CharField(widget=forms.PasswordInput, max_length=20, label="Old Password")
    new_password = forms.CharField(widget=forms.PasswordInput, max_length=20, label="New Password")
    confirm_password = forms.CharField(widget=forms.PasswordInput, max_length=20, label="Confirm Password")

    def __init__(self, *args, **kwargs):
        class_name = kwargs.pop('class_name', None)
        super().__init__(*args, **kwargs)

        if class_name:
            self.fields['student'].queryset = Student.objects.filter(class_name=class_name).order_by('name')

    def clean(self):
        cleaned_data = super().clean()
        old_password = cleaned_data.get("old_password")
        student = cleaned_data.get("student")

        if student and student.password != old_password:
            raise forms.ValidationError('Old password does not match')

        return cleaned_data
