from importlib import import_module
from typing import List, Type, Union

from aiohttp.abc import AbstractView
from aiohttp.hdrs import METH_ANY
from aiohttp.web_routedef import RouteDef


def include(arg) -> List[RouteDef]:
    urlconf_module = arg

    if isinstance(urlconf_module, str):
        urlconf_module = import_module(urlconf_module)

    results: List[RouteDef] = getattr(urlconf_module, 'urlpatterns', urlconf_module)

    return results


def path(route: str, view: Union[Type[AbstractView], List[RouteDef]], **kwargs):

    if isinstance(view, (list, tuple)):

        if not route.endswith('/'):
            route += '/'

        def _recursive(items):
            routes = []
            for pattern in items:
                if not isinstance(pattern, list):
                    routes.append(pattern)
                else:
                    routes += _recursive(pattern)
            return routes

        routes_def = _recursive(view)

        results = [RouteDef(
            method=route_def.method,
            path=(route + route_def.path),
            handler=route_def.handler,
            kwargs=route_def.kwargs)
            for route_def in routes_def]
        return results
    elif callable(view):
        return RouteDef(METH_ANY, route, view, kwargs)
    else:
        raise TypeError('view must be a callable or a list/tuple in the case of include().')
