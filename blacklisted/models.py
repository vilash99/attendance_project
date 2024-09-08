from django.db import models
from datetime import date

from profiles.models import Student, Teacher


class BlackListedStudent(models.Model):
    REASON_CHOICES = (
        ('NOT_PRESENT', 'Not present in class'),
        ('PROXY', 'Marked proxy attendance'),
    )
    student = models.ForeignKey(Student,
                                on_delete=models.CASCADE,
                                default=None)
    teacher = models.ForeignKey(Teacher,
                                on_delete=models.CASCADE,
                                default=None)
    reason = models.CharField(max_length=20,
                              choices=REASON_CHOICES,
                              default=None)
    blacklist_date = models.DateField(default=date.today)

    def __str__(self):
        return self.student.name

    @property
    def reason_text(self):
        return self.get_reason_display()

    class Meta:
        verbose_name_plural = "BlackListStudents"
