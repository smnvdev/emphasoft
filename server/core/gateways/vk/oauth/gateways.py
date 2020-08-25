from typing import Union

from multidict import CIMultiDict
from yarl import URL

from server.core.gateways.base import APIGateway
from server.core.gateways.vk.oauth.schemas import VKOAuthAccessToken

from server.settings import VK_OAUTH_HOST, VK_APP_SECRET_KEY, VK_APP_ID


class VKOAuthBaseGateway(APIGateway):
    api_host = VK_OAUTH_HOST


class VKOAuthGetAccessToken(VKOAuthBaseGateway):
    """Гетвей получения токена авторизации пользователя."""
    url = '/access_token'
    schema = VKOAuthAccessToken()

    def __init__(
            self,
            redirect_uri: Union[URL, str],
            code: str
    ):
        self.query_params: CIMultiDict = CIMultiDict(
            code=code,
            redirect_uri=str(redirect_uri),
            client_secret=VK_APP_SECRET_KEY,
            client_id=VK_APP_ID
        )
