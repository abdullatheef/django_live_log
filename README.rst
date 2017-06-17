=====
Django Live Log
=====

django_live_log is a package which can see live stream of file, such as log file, etc.

Installation
------------

    pip install django_live_log

Quick start
-----------

1. Add "django_live_log" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'django_live_log',
    ]

2. Include the django_live_log URLconf in your project urls.py like this::

    url(r'^dll/', include('django_live_log.urls')),

3. Add "DLL_FILE" to settings.py

4. Visit http://127.0.0.1:8000/dll/ to participate in the poll.


Options
----------

* DLL_URL in settings.py.
    Usage:
      DLL_URL = "/myurl/"
      so dll wii serve at `domain.com/dll/myurl/`

* DLL_GROUP_PERMISSION in settings.py
    Group name or list of group names.
    Usage:
      DLL_GROUP_PERMISSION = "My group name" # or ["My group name1", "My group name2"]

* from
    Start pointer reading from file.
    Usage:
      domain.com/dll/myurl/?from=500

* file_path
    absolute path of file to log
    Usage:
      domain.com/dll/myurl/?file_path=/var/log/myfile.log
    - Should have read permission







