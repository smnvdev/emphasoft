from yarl import URL

from server.core.template.filters import TemplateFilter
from server.settings import VK_OAUTH_HOST, VK_APP_ID, OAUTH_REDIRECT_URI


class OAuthVKLinkGenerationFilter(TemplateFilter):
    """
    Генерирует ссылку для OAuth авторизации.
    """

    name = 'oauth_vk_link'

    vk_method = '/authorize'

    def filter(self, *args, **kwargs):
        scheme, host = VK_OAUTH_HOST.split('://')
        url = URL.build(
            scheme=scheme,
            host=host,
            path=self.vk_method,
            query=dict(
                client_id=VK_APP_ID,
                redirect_uri=OAUTH_REDIRECT_URI,
                display='page',
                scope='friends',
                response_type='code',
                v='5.122'
            )
        )
        return str(url)
