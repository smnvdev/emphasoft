from typing import Union

from yarl import URL

from server.core.base.dto import DTO
from server.core.base.facades import BaseFacade
from server.core.gateways.vk.oauth.dto import VkOAuthAccessTokenDTO
from server.core.gateways.vk.oauth.gateways import VKOAuthGetAccessToken


class OAuthGetAccessTokenFacadeContext(DTO):
    access_token: VkOAuthAccessTokenDTO


class OAuthGetAccessTokenFacade(BaseFacade):

    context = OAuthGetAccessTokenFacadeContext

    def __init__(
            self,
            redirect_uri: Union[URL, str],
            code: str
    ):
        self.gateways = dict(
            access_token=VKOAuthGetAccessToken(
                redirect_uri=redirect_uri,
                code=code
            )
        )

    @staticmethod
    def process_context(context: OAuthGetAccessTokenFacadeContext) -> VkOAuthAccessTokenDTO:
        return context.access_token
