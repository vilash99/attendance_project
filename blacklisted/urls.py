from django.urls import path

from .views import blacklist_add, remove_blacklist

app_name = 'blacklisted'

urlpatterns = [
    path('blacklist_student/<int:entry_id>/<int:std_id>/<int:att_id>',
         blacklist_add, name='blacklist_student'),
    path('remove_blacklist/', remove_blacklist, name='remove_blacklist'),
]
