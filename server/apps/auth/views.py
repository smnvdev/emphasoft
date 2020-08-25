from aiohttp.web_exceptions import HTTPBadRequest, HTTPFound

from server.apps.auth.facades import OAuthGetAccessTokenFacade
from server.core.base.views import BaseView
from server.core.gateways.vk.oauth.dto import VkOAuthAccessTokenDTO
from server.core.middleware.authenticate import authorize, anonymous_required, logout
from server.core.redis.users import VKAccessTokenObjectManager
from server.settings import OAUTH_REDIRECT_URI


class OAuthSignInView(BaseView):

    template = 'auth/index.html'

    @anonymous_required('index')
    async def get(self):
        return await self.render()


class LogOutView(BaseView):

    async def get(self):
        return logout(
            self.request,
            HTTPFound(
                location=self.request.app.router['auth-signin'].url_for()
            )
        )


class OAuthCallbackView(BaseView):

    template = 'callback/index.html'

    async def get(self):
        code = self.request.query.getone('code', None)

        if code is None:
            return HTTPBadRequest()

        self.facade = OAuthGetAccessTokenFacade(
            redirect_uri=OAUTH_REDIRECT_URI,
            code=code
        )

        access_token: VkOAuthAccessTokenDTO = await self.context

        return await authorize(
            self.request,
            self._render(self.template),
            access_token
        ) # TODO - надо рендерить страницу которая по таймеру закрывается. Как только она закроется управление получает основная страница входа и рефрешится
