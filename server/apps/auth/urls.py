from server.apps.auth.views import OAuthSignInView, OAuthCallbackView, LogOutView
from server.core.common.urls import path

urlpatterns = [
    path('sign-in', OAuthSignInView, name='auth-signin'),
    path('exit', LogOutView, name='auth-logout'),
    path('callback', OAuthCallbackView, name='auth-callback')
]
