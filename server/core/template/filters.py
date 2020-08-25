from abc import ABC, abstractmethod
from typing import Optional

from aiohttp.abc import Application


class TemplateFilter(ABC):

    name: str

    def __init__(self, app: Optional[Application] = None):
        self.app = app

    def __call__(self, *args, **kwargs):
        return self.filter(*args, **kwargs)

    @abstractmethod
    def filter(self, *args, **kwargs):
        pass
