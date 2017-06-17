from django.conf.urls import url
from django.conf import settings
from django_live_log.views import dll
urlpatterns = [
    url(r'^%s$' %('%s/' %getattr(settings, "DLL_URL", "").strip("/") if getattr(settings, "DLL_URL", "") else ""), dll, name="dll"),
]