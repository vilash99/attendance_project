from django.urls import path
from .views import EntryCreateView, GenerateToken

urlpatterns = [
    path('entries/', EntryCreateView.as_view(), name='entry_create'),
    path('generate-token/', GenerateToken.as_view(), name='generate_token'),
]
