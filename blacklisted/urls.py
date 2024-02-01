from django.urls import path

from .views import BlackListCreateView, remove_blacklist

app_name = 'blacklisted'

urlpatterns = [
    path('blacklist_student/<int:entry_id>/<int:std_id>/<int:att_id>',
         BlackListCreateView.as_view(), name='blacklist_student'),
    path('remove_blacklist/', remove_blacklist, name='remove_blacklist'),
]
