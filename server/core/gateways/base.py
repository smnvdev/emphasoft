from abc import ABC
from typing import Any, Dict, Mapping, Optional

from aiohttp import ClientResponse, ClientResponseError, ClientSession
from aiohttp.typedefs import LooseHeaders
from yarl import URL

from server.core.base.dto import DTO
from server.core.base.schema import BaseSchema


class BaseGateway(ABC):
    """Абстрактный шлюз."""


class HTTPGateway(BaseGateway):
    """HTTP шлюз."""


class APIGateway(HTTPGateway):
    """ API шлюз. """
    api_host: str

    url: str
    method: str = 'GET'
    query_params: Optional[Mapping[str, str]] = None
    headers: LooseHeaders = None
    raise_for_status: Optional[bool] = True
    data: Any = None
    json: Any = None
    request_kwargs: Optional[Dict[str, Any]] = None
    schema: BaseSchema

    async def process_response(self, response: ClientResponse) -> DTO:
        """Пост обработка данных с API."""
        data = await response.json()
        return self.schema.load(data)

    async def process_response_error(self, error: ClientResponseError):
        """Обработка ошибок при запросе к API"""
        raise error

    def get_url(self):
        return URL(self.api_host).with_path(self.url)

    def _request_params(self):
        params = dict(
            method=self.method,
            headers=self.headers,
            url=self.get_url(),
            params=self.query_params,
            raise_for_status=True,
            data=self.data,
            json=self.json
        )
        if self.request_kwargs is not None:
            params.update(**self.request_kwargs)
        return params

    async def execute(self, session: ClientSession):
        try:
            params = self._request_params()
            async with session.request(**params) as response:
                result = await self.process_response(response)
                return result
        except ClientResponseError as error:
            return await self.process_response_error(error)
