from marshmallow import fields, post_load

from server.core.base.schema import BaseSchema
from server.core.gateways.vk.oauth.dto import VkOAuthAccessTokenDTO


class VKOAuthAccessToken(BaseSchema):
    access_token = fields.String()
    expires_in = fields.Integer()
    user_id = fields.Integer()
    email = fields.String(required=False, default=None)

    @post_load
    def make_dto(self, data, **kwargs):
        return VkOAuthAccessTokenDTO(**data)
