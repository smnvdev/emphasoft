import pickle
from typing import Optional

from server.core.common.crypto import get_random_secret_key
from server.core.gateways.vk.oauth.dto import VkOAuthAccessTokenDTO
from server.core.redis.base import BaseObjectStoreManager


class VKAccessTokenObjectManager(BaseObjectStoreManager):

    key = '{key}__vk__access_token'

    async def set_access_token(
            self,
            access_token: VkOAuthAccessTokenDTO,
    ) -> str:
        t_key = get_random_secret_key()
        key = self.key.format(key=t_key)
        await self._store.set(
            key=key,
            value=pickle.dumps(
                access_token
            ),
            expire=access_token.expires_in
        )
        return t_key

    async def get_access_token(
            self,
            t_key: str,
    ) -> Optional[VkOAuthAccessTokenDTO]:
        key = self.key.format(key=t_key)
        if await self._store.exists(key=key) == 1:
            return pickle.loads(
                await self._store.get(
                    key=key
                )
            )
        return None

    async def exists_access_token(
            self,
            t_key: str
    ) -> bool:
        key = self.key.format(key=t_key)
        return await self._store.exists(key=key) == 1

    async def delete_access_token(
            self,
            t_key: str
    ) -> bool:
        key = self.key.format(key=t_key)
        return await self._store.delete(
            key=key
        )
