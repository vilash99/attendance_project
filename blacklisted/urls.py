from django.urls import path

from .views import blacklist_student, remove_blacklist

app_name = 'blacklisted'

urlpatterns = [
    path('blacklist_student/', blacklist_student, name='blacklist_student'),
    path('remove_blacklist/', remove_blacklist, name='remove_blacklist'),
]
