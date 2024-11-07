from django.urls import path
from .views import EntryCreateView, GenerateToken, ClassStudentsView

urlpatterns = [
    path('entries/', EntryCreateView.as_view(), name='entry_create'),
    path('generate-token/', GenerateToken.as_view(), name='generate_token'),
    path('class-students/', ClassStudentsView.as_view(), name='class_students'),
]
