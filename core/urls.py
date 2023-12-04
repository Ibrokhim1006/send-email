from django.contrib import admin
from django.urls import path
from send_email.views import CheckEmailCode
admin.site.site_url = None

urlpatterns = [
    path('admin/', admin.site.urls),
    path('send_email/', CheckEmailCode.as_view(), name='send_email'),
]
