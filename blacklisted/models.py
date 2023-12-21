from django.db import models

from profiles.models import Student


class BlackListedStudent(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return self.student.name

    class Meta:
        verbose_name_plural = "BlackListStudents"
