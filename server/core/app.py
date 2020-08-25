import logging
from importlib import import_module
from typing import Optional, Iterable, Callable, Dict, Type

from aiohttp.web import Application
from aiohttp.web_routedef import AbstractRouteDef
from jinja2 import FileSystemLoader

from server import settings
from server.core.redis.manager import StoresManager
from server.core.template import TemplateEngine, context_processor
from server.core.template.filters import TemplateFilter
from server.urls import urlpatterns


async def create_application():
    application = CoreApplication()
    stores = await StoresManager.create(application)
    application.stores = stores
    logging.basicConfig(level=logging.DEBUG)
    return application


class CoreApplication(Application):
    """Основное приложение aiohttp"""
    stores: Optional[StoresManager] = None

    def __init__(self, *args, **kwargs):
        kwargs.update({
            'middlewares': self._create_middleware()
        })
        super().__init__(**kwargs)
        self.__setup_web_template_engine()
        r = self.create_routes()
        self.add_routes(r)

    def __setup_web_template_engine(self):
        """Инициализация шаблонизатора."""
        self.engine = TemplateEngine(
            app=self,
            loader=FileSystemLoader(settings.TEMPLATES_ROOT),
            context_processors=[
                context_processor,
            ],
            filters=self._create_template_filters(),
        )
        self['static_root_url'] = settings.STATIC_URL

    @staticmethod
    def _create_template_filters() -> Dict[str, Type[TemplateFilter]]:
        filters = {}
        for path in settings.TEMPLATE_FILTERS:
            module, cls_name = path.rsplit('.', 1)
            cls = getattr(import_module(module), cls_name)
            instance = cls()
            filters.update({instance.name: instance})
        return filters

    @staticmethod
    def _create_middleware() -> Iterable[Callable]:
        middleware = []
        for path in settings.MIDDLEWARE:
            module, cls_name = path.rsplit('.', 1)
            cls = getattr(import_module(module), cls_name)
            middleware.append(cls())
        return middleware

    @staticmethod
    def create_routes():
        def _recursive(urls):
            routes = []
            for route in urls:
                if isinstance(route, AbstractRouteDef):
                    routes.append(route)
                else:
                    routes += _recursive(route)
            return routes

        return _recursive(urlpatterns)
