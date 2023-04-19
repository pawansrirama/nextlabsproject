from django.urls import path,include,re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve 


urlpatterns = [
path('',views.admin_login,name='admin_login'),
path('loginauth/',views.admin_page,name='admin_page'),
path('invalidcredentials/',views.invaild_log,name='invaild_log'),
re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
