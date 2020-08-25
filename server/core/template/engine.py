from typing import Any, Callable, Dict, Iterable, Optional, Union

from aiohttp.abc import Application
from aiohttp.web import Request
from aiohttp_jinja2 import setup
from jinja2 import BaseLoader
from jinja2.ext import Extension


class TemplateEngine:

    def __init__(
            self,
            app: Application,
            *,
            loader: Optional[BaseLoader] = None,
            context_processors: Iterable[Callable[[Request], Dict[str, Any]]] = (),
            filters: Optional[Iterable[Callable[..., str]]] = None,
            extensions: Optional[Union[Iterable[str], Iterable[Extension]]] = []
    ):
        self.filters = filters

        self.env = setup(
            app=app,
            loader=loader,
            context_processors=context_processors,
            filters=filters,
            extensions=extensions,
            trim_blocks=True,
            lstrip_blocks=True
        )
