from server.core.base.dto import DTO
from server.core.base.facades import BaseFacade
from server.core.gateways.vk.api.dto import ResponseDTO
from server.core.gateways.vk.api.friends.enums import VKFriendsOrderEnum, VKFriendsAdditionalField
from server.core.gateways.vk.api.friends.gateways import VKGetUserFriendsGateway


class VKGetFriendsContext(DTO):
    friends: ResponseDTO


class VKGetFiveRandomFriendsFacade(BaseFacade):

    context = VKGetFriendsContext

    def __init__(self, access_token: str):
        self.gateways = dict(
            friends=VKGetUserFriendsGateway(
                access_token=access_token,
                order=VKFriendsOrderEnum.RANDOM,
                count=5,
                fields=[
                    VKFriendsAdditionalField.PHOTO_200_ORIG,
                    VKFriendsAdditionalField.CITY,
                    VKFriendsAdditionalField.DOMAIN,
                    VKFriendsAdditionalField.PHOTO_100
                ]
            )
        )

    @staticmethod
    def process_context(context: VKGetFriendsContext):
        return context.friends.response.items
