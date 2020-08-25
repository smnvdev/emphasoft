from typing import List

from server.apps.index.facades import VKGetFiveRandomFriendsFacade
from server.core.base.views import BaseView
from server.core.gateways.vk.api.friends.dto import VKFriendDTO
from server.core.middleware.authenticate import login_required

from aiohttp_jinja2 import render_template as render


class IndexPageView(BaseView):

    template = 'index/index.html'

    @login_required(redirect_field_name='auth-signin')
    async def get(self):
        # TODO: отправляем запрос на получение друзей
        # TODO: при ошибке редиректим на авторизацию

        self.facade = VKGetFiveRandomFriendsFacade(
            access_token=self.request['access_token'].access_token
        )

        friends: List[VKFriendDTO] = await self.context

        return render(
            template_name=self.template,
            request=self.request,
            context=dict(
                friends=friends
            )
        )
