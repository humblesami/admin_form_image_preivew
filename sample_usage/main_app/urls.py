from django.contrib import admin
from django.conf import settings
from django.views.static import serve
from django.urls import re_path



def define_pth():
    pth_prefix = settings.PATH_PREFIX or ''
    if pth_prefix:
        pth_prefix += '/'
    media_root = {'document_root': settings.MEDIA_ROOT}
    media_pth = [re_path(r'^' + pth_prefix + 'media/(?P<path>.*)$', serve, media_root)]

    static_root = {'document_root': settings.STATIC_ROOT}
    static_pth = [re_path(r'^' + pth_prefix + 'static/(?P<path>.*)$', serve, static_root)]

    # admin.autodiscover()
    if pth_prefix:
        pth_prefix = r'^'+pth_prefix
    app_pth = [
        re_path(pth_prefix + 'admin/', admin.site.urls),
    ]
    all_pth = media_pth + static_pth + app_pth
    return all_pth


urlpatterns = define_pth()
