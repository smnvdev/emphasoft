from aiohttp.web_routedef import static

from server.apps.index.urls import urlpatterns as index_urlpatterns
from server.apps.auth.urls import urlpatterns as auth_urlpatterns
from server.core.common.urls import path
from server.settings import DEBUG, STATIC_ROOT


urlpatterns = [
    path('', index_urlpatterns),
    path('/auth', auth_urlpatterns)
]

if DEBUG:
    urlpatterns += [
        static('/static/', path=str(STATIC_ROOT), name='static'),
    ]
