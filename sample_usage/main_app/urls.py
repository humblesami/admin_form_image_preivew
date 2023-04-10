from django.urls import re_path
from django.conf import settings
from django.contrib import admin




def define_pth():
    pth_prefix = settings.PATH_PREFIX or ''
    if pth_prefix:
        pth_prefix += '/'

    # admin.autodiscover()
    if pth_prefix:
        pth_prefix = r'^'+pth_prefix
    app_pth = [
        re_path(pth_prefix + 'admin/', admin.site.urls),
    ]
    return app_pth


urlpatterns = define_pth()
