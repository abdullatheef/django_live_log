from django.contrib.auth.decorators import user_passes_test
import os, time
from django.http import StreamingHttpResponse
from django.template import Context, loader
from django.conf import settings

def log_streamer(request, from_=0, file_path=None):
    try:
        file_path = file_path or settings.DLL_FILE
        mtime = os.path.getmtime(file_path)
        with open(file_path) as f:
            start = -int(from_) or -2000
            filestart = True
            while filestart:
                try:
                    f.seek(start, 2)
                    filestart = False
                    result = f.read()
                    last = f.tell()
                    t = loader.get_template('django_live_log/main.html')
                    yield t.render(Context({"result": result}))
                except IOError:
                    start += 50
        reset = 0
        while True:
            newmtime = os.path.getmtime(file_path)
            if newmtime == mtime:
                time.sleep(1)
                reset += 1
                if reset >= 15:
                    yield "<!-- empty -->"
                continue
            mtime = newmtime
            with open(file_path) as f:
                f.seek(last)
                result = f.read()
                if result:
                    t = loader.get_template('django_live_log/main.html')
                    yield result + "<script>$('html,body').animate({ scrollTop: $(document).height() }, 'slow');</script>"
                last = f.tell()
    except Exception as e:
        import traceback
        print(traceback.format_exc())


def dll(request):
    return StreamingHttpResponse(log_streamer(request, request.GET.get('from', 1000), request.GET.get('file_path', "")))

def group_check(user):
    return user.groups.filter(
        name__in=settings.DLL_GROUP_PERMISSION if isinstance(settings.DLL_GROUP_PERMISSION, list) else [settings.DLL_GROUP_PERMISSION])

if getattr(settings, "DLL_GROUP_PERMISSION", ""):
    dll = user_passes_test(group_check)(dll)
