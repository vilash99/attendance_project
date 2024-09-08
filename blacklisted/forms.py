from django import forms
from .models import BlackListedStudent
from profiles.models import Student
from attendance.models import Entry


class BlackListStudentForm(forms.ModelForm):
    class Meta:
        model = BlackListedStudent
        fields = ['student', 'teacher', 'reason']

    def __init__(self, entry_id, std_id, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.entry_id = entry_id
        self.std_id = std_id

        self.fields['student'].queryset = Student.objects.filter(
            pk=std_id)

    def save(self, commit=True):
        instance = forms.ModelForm.save(self, True)

        # Delete entry from attendance entry
        entry_obj = Entry.objects.get(id=self.entry_id)
        entry_obj.delete()

        return instance
