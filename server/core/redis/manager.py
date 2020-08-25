from aioredis import Redis, create_redis_pool

from server.core.redis.users import VKAccessTokenObjectManager
from server.settings import REDIS_URL, REDIS_DB_INDEX


class StoresManager:

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
        return cls.instance

    @classmethod
    async def create(cls, app):
        if not hasattr(cls, 'instance'):
            cls.instance = StoresManager(app)
            await cls.instance._init_store()
        return cls.instance

    def __init__(self, app):
        self.__app = app

    @staticmethod
    def close_connections(pool):
        async def _close(app):
            pool.close()
            await pool.wait_closed()

        return _close

    async def _init_store(self):
        self._pool: Redis = await create_redis_pool(
            address=REDIS_URL,
            db=REDIS_DB_INDEX
        )

        self.access_tokens = VKAccessTokenObjectManager(self.__app, self._pool)

        self.__app.on_cleanup.append(self.close_connections(self._pool))
