from django.db import models
from django.urls import reverse
from .classes import CLASS_NAMES


class Teacher(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('profiles:teacher_detail', args=[self.id])


class Student(models.Model):
    name = models.CharField(max_length=100)
    class_name = models.CharField(max_length=30, choices=CLASS_NAMES)
    password = models.CharField(max_length=20, default='abc123')

    def __str__(self):
        return self.name

    @property
    def class_full_name(self):
        return self.get_class_name_display()

    def get_absolute_url(self):
        return reverse('profiles:student_detail', args=[self.id])
