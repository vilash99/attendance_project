from django.urls import path
from .views import EntryCreateView

urlpatterns = [
    path('entries/', EntryCreateView.as_view(), name='entry_create'),
]
