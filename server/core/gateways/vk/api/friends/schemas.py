from marshmallow import fields, post_load

from server.core.base.schema import BaseSchema
from server.core.gateways.vk.api.friends.dto import VKCityDTO, VKFriendDTO


class VKCitySchema(BaseSchema):
    id = fields.Integer()
    title = fields.String()

    @post_load
    def make_dto(self, data, **kwargs):
        return VKCityDTO(**data)


class VKFriendSchema(BaseSchema):
    id = fields.Integer()
    first_name = fields.String()
    last_name = fields.String()
    is_closed = fields.Boolean()
    can_access_closed = fields.Boolean()

    online = fields.Integer()
    track_code = fields.String()

    nickname = fields.String()
    domain = fields.String()
    sex = fields.Integer()
    bdate = fields.String()
    city = fields.Nested(
        nested=VKCitySchema
    )

    photo_50 = fields.String()
    photo_100 = fields.String()
    photo_200_orig = fields.String()

    @post_load
    def make_dto(self, data, **kwargs):
        return VKFriendDTO(**data)
