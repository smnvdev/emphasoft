from abc import ABC
from typing import Optional

from aiohttp.web import Application
from aioredis import Redis, create_redis_pool


class BaseObjectStoreManager(ABC):
    _app: Application
    _store: Optional[Redis] = None

    def __init__(self, app: Application, store: Optional[Redis] = None):
        self._app = app
        self._store = store

    async def create_pool(self, redis_url: str, db: int):
        self._store = await create_redis_pool(
            address=redis_url,
            db=db
        )
