from abc import ABC, abstractmethod
from functools import partial
from typing import Callable, Any, Awaitable

from aiohttp.abc import StreamResponse, BaseRequest
from aiohttp.web import Application

from server import core


class BaseMiddleware(ABC):

    def _after_set_app(self):
        """Инициализация после установки self._app."""

    async def __call__(self, app: Application, handler: partial):
        self._app: core.CoreApplication = app
        self._after_set_app()
        return partial(self.middleware, handler)

    @staticmethod
    def save_to_request_storage(request: BaseRequest, **kwargs) -> None:
        for key, value in kwargs.items():
            request[key] = value

    @abstractmethod
    async def middleware(self, handler: Callable[[Any], Awaitable[StreamResponse]], request: BaseRequest):
        """Основной метод middleware"""
        raise NotImplementedError
