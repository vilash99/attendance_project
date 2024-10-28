# api/serializers.py
from rest_framework import serializers
from attendance.models import Entry, Student
from blacklisted.models import BlackListedStudent


class EntrySerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    unique_code = serializers.IntegerField(write_only=True)
    class_name = serializers.CharField(write_only=True)

    class Meta:
        model = Entry
        fields = ['student', 'password', 'unique_code', 'attendance', 'class_name']

    def validate_password(self, value):
        # Validate that the default password is not used
        if value == 'abc123':
            raise serializers.ValidationError('Default password is not allowed! Please change your password.')
        return value

    def validate(self, data):
        student = data.get('student')
        password = data.get('password')
        unique_code = int(data.get('unique_code'))
        attendance = data.get('attendance')
        active_class = data.get('class_name')

        # Check if the student exists and validate the password
        if not Student.objects.filter(class_name=active_class, id=student.id, password=password).exists():
            raise serializers.ValidationError('Incorrect password! Please try again.')

        # Ensure the student has not already marked attendance
        if Entry.objects.filter(attendance=attendance, student=student).exists():
            raise serializers.ValidationError('You have already marked attendance for this subject!')

        # Validate unique code
        if attendance.unique_code != unique_code:
            raise serializers.ValidationError('Incorrect unique code!')

        # Ensure not exceeding total students
        total_present = Entry.objects.filter(attendance=attendance).count()
        if total_present >= attendance.total_students:
            raise serializers.ValidationError('Your attendance is not saved. Because all students have given attendance. Ask the teacher to resolve this issue.')

        # Check if the student is blacklisted
        if BlackListedStudent.objects.filter(student=student).exists():
            raise serializers.ValidationError('You are BLACKLISTED and cannot mark attendance.')

        return data

    def create(self, validated_data):
        validated_data.pop('password')
        validated_data.pop('unique_code')
        validated_data.pop('class_name')

        # Create a new Entry instance
        return super().create(validated_data)

