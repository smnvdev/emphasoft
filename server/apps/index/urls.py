from server.apps.index.views import IndexPageView
from server.core.common.urls import path


urlpatterns = [
    path('', IndexPageView, name='index')
]
