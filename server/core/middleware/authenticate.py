import asyncio
from typing import Callable, Any, Awaitable, Union, Optional

from aiohttp.abc import StreamResponse, BaseRequest
from aiohttp.web import View
from aiohttp.web_exceptions import HTTPFound
from aiohttp.web_response import Response

from server.core.gateways.vk.oauth.dto import VkOAuthAccessTokenDTO
from server.core.middleware.base import BaseMiddleware
from server.core.redis.users import VKAccessTokenObjectManager
from server.settings import AUTH_COOKIE_NAME


class VKOAuthMiddleware(BaseMiddleware):

    REQUEST_STORE_NAME = 'access_token'
    COOKIE_NAME = AUTH_COOKIE_NAME

    @property
    def store(self) -> VKAccessTokenObjectManager:
        return self._app.stores.access_tokens

    async def middleware(self, handler: Callable[[Any], Awaitable[StreamResponse]], request: BaseRequest):
        auth_cookie = request.cookies.get(self.COOKIE_NAME, None)
        if auth_cookie:
            request[self.REQUEST_STORE_NAME] = await self.store.get_access_token(auth_cookie)
        else:
            request[self.REQUEST_STORE_NAME] = None
        return await handler(request)


def login_required(redirect_field_name: Optional[str] = None):
    """Login Required Decorator"""

    def inner(function):
        async def wrapper(view_or_request: Union[View, BaseRequest]):
            request = view_or_request.request if isinstance(view_or_request, View) else view_or_request
            auth_cookie: Optional[str] = request.cookies.get(AUTH_COOKIE_NAME, None)

            if auth_cookie is not None:
                store: VKAccessTokenObjectManager = request.app.stores.access_tokens
                if await store.exists_access_token(t_key=auth_cookie):
                    return await function(view_or_request)

            raise HTTPFound(
                location=request.app.router[redirect_field_name].url_for()
            )
        return wrapper
    return inner


def anonymous_required(redirect_field_name: Optional[str] = None):
    """Anonymous Required Decorator"""

    def inner(function):
        async def wrapper(view_or_request: Union[View, BaseRequest]):
            request = view_or_request.request if isinstance(view_or_request, View) else view_or_request
            auth_cookie: Optional[str] = request.cookies.get(AUTH_COOKIE_NAME, None)

            if auth_cookie is None:
                return await function(view_or_request)
            else:
                store: VKAccessTokenObjectManager = request.app.stores.access_tokens
                if not await store.exists_access_token(t_key=auth_cookie):
                    return await function(view_or_request)

            raise HTTPFound(
                location=request.app.router[redirect_field_name].url_for()
            )
        return wrapper
    return inner


async def authorize(request, response: Response, vk_access_token: VkOAuthAccessTokenDTO):
    """Авторизация пользователя"""
    store: VKAccessTokenObjectManager = request.app.stores.access_tokens
    auth_token = await store.set_access_token(vk_access_token)
    response.set_cookie(
        name=AUTH_COOKIE_NAME,
        value=auth_token,
        expires=vk_access_token.expires_in
    )
    return response


def logout(request, response: Response,):
    """Деавторизация пользователя."""
    auth_cookie: Optional[str] = request.cookies.get(AUTH_COOKIE_NAME, None)
    if auth_cookie:
        store: VKAccessTokenObjectManager = request.app.stores.access_tokens
        asyncio.get_event_loop().create_task(
            store.delete_access_token(auth_cookie)
        )
        response.del_cookie(
            name=AUTH_COOKIE_NAME
        )
    return response
