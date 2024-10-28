from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from attendance.models import Attendance
from profiles.models import Student
from .serializers import EntrySerializer


class EntryCreateView(APIView):
    def get(self, request):
        class_name = request.query_params.get('class_name')

        if not class_name:
            return Response({'error': 'class_name parameter is required.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Retrieve active attendance based on the class name
            attendance = Attendance.objects.get(class_name=class_name, is_active=True)

            # Fetch all students in the class
            students = Student.objects.filter(class_name=class_name).order_by('name')

            response_data = {
                'attendance': attendance.id,
                'students': [{'id': student.id, 'name': student.name} for student in students],
            }
            return Response(response_data, status=status.HTTP_200_OK)

        except Attendance.DoesNotExist:
            return Response({'error': 'No active attendance found for this class.'}, status=status.HTTP_404_NOT_FOUND)


    def post(self, request):
        class_name = request.data.get('class_name')

        if not class_name:
            return Response({'error': 'class_name parameter is required.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Check if there's an active attendance for the specified class_name
            attendance = Attendance.objects.get(class_name=class_name, is_active=True)

            # If active attendance found, proceed to validate and create the entry
            serializer = EntrySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(attendance=attendance)
                return Response({'message': 'Attendance marked successfully!'}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Attendance.DoesNotExist:
            return Response({'error': 'No active attendance found for this class.'}, status=status.HTTP_404_NOT_FOUND)


