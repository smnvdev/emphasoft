from typing import Optional, List

from marshmallow.fields import Integer

from server.core.gateways.vk.api.friends.dto import VKFriendDTO
from server.core.gateways.vk.api.friends.enums import VKFriendsOrderEnum, VKFriendsAdditionalField, VKNameCase
from server.core.gateways.vk.api.friends.schemas import VKFriendSchema
from server.core.gateways.vk.api.gateways import VKAPIGateway
from server.core.gateways.vk.api.schemas import response_schema


class VKGetUserFriendsGateway(VKAPIGateway):
    """
    Cписок идентификаторов друзей пользователя
    или расширенную информацию о друзьях пользователя.
    """
    vk_method_name = 'friends.get'
    schema = response_schema(Integer(), int)()

    def __init__(
            self,
            access_token: str,
            *,
            user_id: Optional[int] = None,
            order: Optional[VKFriendsOrderEnum] = None,
            list_id: Optional[int] = None,
            count: Optional[int] = None,
            offset: Optional[int] = None,
            fields: Optional[List[VKFriendsAdditionalField]] = None,
            name_case: Optional[VKNameCase] = None,
            version: Optional[str] = '5.122'
    ):
        query_params = dict(
            access_token=access_token,
            v=version
        )
        if user_id is not None:
            query_params.update(dict(
                user_id=user_id
            ))
        if order is not None:
            query_params.update(dict(
                order=order.value
            ))
        if list_id is not None:
            query_params.update(dict(
                list_id=list_id
            ))
        if count is not None:
            query_params.update(dict(
                count=count
            ))
        if offset is not None:
            query_params.update(dict(
                offset=offset
            ))
        if fields is not None:
            query_params.update(dict(
                fields=','.join([field.value for field in fields])
            ))
            self.schema = response_schema(VKFriendSchema(), VKFriendDTO)()
        if name_case is not None:
            query_params.update(dict(
                name_case=name_case.value
            ))

        self.query_params = query_params
