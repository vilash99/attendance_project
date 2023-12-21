from django.db import models
from datetime import date
from django.urls import reverse

from profiles.models import Teacher, Student
from profiles.classes import *


class Attendance(models.Model):
    att_date = models.DateField(default=date.today)
    teacher = models.ManyToManyField(Teacher)
    subject_name = models.CharField(max_length=50)
    class_name = models.CharField(max_length=50, choices=CLASS_NAMES)
    unique_code = models.IntegerField(default=0)
    total_students = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{str(self.att_date)} {self.subject_name}'

    @property
    def class_full_name(self):
        return self.get_class_name_display()

    def get_absolute_url(self):
        return reverse('attendance:attendances_detail', args=[str(self.id)])


class Entry(models.Model):
    attendance = models.ForeignKey(Attendance, on_delete=models.CASCADE)
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, verbose_name='Student name')

    def __str__(self):
        return self.student.name

    def get_absolute_url(self):
        return reverse('attendance:success')

    class Meta:
        verbose_name_plural = "Entries"
