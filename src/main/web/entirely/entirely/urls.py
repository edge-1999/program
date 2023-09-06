"""entirely URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.views import serve
from django.urls import path, include, re_path

# 站点标题
admin.site.site_title = '小李的窝'  # 网站标签页名称
admin.site.site_header = '李思源的老窝'  # 网站名称：显示在登录页和首页

urlpatterns = [
    path('sp/', include('simplepro.urls')),
    path(settings.ADMIN_URL_ZDY, admin.site.urls),
    path('', include('menu_management.urls', namespace='menu_management')),
    path('account/', include('account_management.urls', namespace='account_management')),
    # re_path(r'^docs/static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    # re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings_entirely.MEDIA_ROOT}),
    # path('favicon.ico', RedirectView.as_view(url=r'docs/static/images/favicon.svg')),
    # path('favicon', RedirectView.as_view(url=r'docs/static/images/favicon.svg')),
    # path('null_svg', RedirectView.as_view(url=r'docs/static/images/null.svg')),
    # path('admin_png', RedirectView.as_view(url=r'docs/static/images/19990929.jpg')),
    # re_path(r'$', DjangoHome.as_view()),
]
if settings.DEBUG:
    # urlpatterns += static(settings_entirely.MEDIA_URL, document_root=settings_entirely.MEDIA_ROOT)
    # urlpatterns += staticfiles_urlpatterns()  # from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += static(settings.STATIC_URL, view=serve)
else:
    # urlpatterns += static(settings_entirely.MEDIA_URL, document_root=settings_entirely.MEDIA_ROOT) + static(
    #     settings_entirely.STATIC_URL)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL)
# handler400 = bad_request
# handler403 = permission_denied
# handler404 = page_not_found
# handler500 = server_error
