###############################################################################
from django.contrib import admin
from django.urls import path, include

from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('attendance.urls')),
    path('profiles/', include('profiles.urls')),
    path('blacklisted/', include('blacklisted.urls')),
    path('promotion/', include('promotion.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('api/', include('api.urls')),

    path('favicon.ico', RedirectView.as_view(
        url=staticfiles_storage.url('images/favicon.ico'))),
]

handler500 = 'profiles.views.error_500'
handler404 = 'profiles.views.error_404'
