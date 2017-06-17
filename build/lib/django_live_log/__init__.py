from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

try:
    settings.DLL_FILE
except:
    raise ImproperlyConfigured("Since you are using `django_live_dbug`, set the log file in settings as `DLL_FILE`")

