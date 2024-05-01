from django.contrib import admin
from django.urls import path, include
from django.conf import settings


handler404='diplom.views.page_not_found'

handler500='diplom.views.server_error'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/', include("api.urls")),
    path('', include("diplom.urls"))
]

if settings.DEBUG:
    import debug_toolbar
    # Добавить к списку urlpatterns список адресов из приложения debugtoolbar:
    urlpatterns += (path('__debug/', include(debug_toolbar.urls)),)