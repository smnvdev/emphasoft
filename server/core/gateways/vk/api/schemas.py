from typing import Type, Union

from marshmallow import fields, post_load

from server.core.base.dto import DTO
from server.core.base.schema import BaseSchema
from server.core.gateways.vk.api.dto import ResponseContentDTO, ResponseDTO


def response_schema(schema: Type[BaseSchema], dto: Union[Type[DTO], Type]) -> Type[BaseSchema]:
    """Декорирует схему для пагинации объектов."""

    class ResponseContentSchema(BaseSchema):
        count = fields.Integer()
        items = fields.List(
            fields.Nested(
                schema
            )
        )

        @post_load
        def make_dto(self, data, **kwargs):
            return ResponseContentDTO[dto](**data)

    class ResponseSchema(BaseSchema):
        response = fields.Nested(
            ResponseContentSchema
        )

        @post_load
        def make_dto(self, data, **kwargs):
            return ResponseDTO(**data)

    return ResponseSchema
