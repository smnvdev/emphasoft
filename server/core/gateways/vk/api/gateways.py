from urllib.parse import urljoin

from server.core.gateways.base import APIGateway
from server.settings import VK_API_HOST


class VKAPIGateway(APIGateway):
    api_host = VK_API_HOST
    url = 'method/'
    vk_method_name: str

    def get_url(self):
        self.url = urljoin(self.url, self.vk_method_name.lstrip('/'))
        return super().get_url()
