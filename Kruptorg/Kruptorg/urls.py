from django.contrib import admin
from django.urls import path, include, re_path
from drf_yasg.views import get_schema_view
from django.conf import settings
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title = 'Kruptorg api',
        default_version = 'v1',
        description = 'Документация для сайта',
    ),
    permission_classes = (permissions.AllowAny, ),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/', include("api.urls")),
    path('', include("diplom.urls"))
]

urlpatterns += [
    re_path(r'^swagger(?P<format>.json|.yaml)$',
       schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0),
       name='schema-swagger-ui'),
]

handler404 = 'diplom.views.page_not_found'

handler500 = 'diplom.views.server_error'

handler403 = 'diplom.views.csrf_failure'

if settings.DEBUG:
    import debug_toolbar
    # Добавить к списку urlpatterns список адресов из приложения debugtoolbar:
    urlpatterns += (path('__debug/', include(debug_toolbar.urls)),)