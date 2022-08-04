from django.urls import re_path
from django.conf import settings
from django_live_log.views import dll
urlpatterns = [
    re_path(r'^%s$' %('%s/' %getattr(settings, "DLL_URL", "").strip("/") if getattr(settings, "DLL_URL", "") else ""), dll, name="dll"),
]
