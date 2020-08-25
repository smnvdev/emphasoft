from typing import Optional, Union, Dict

from aiohttp.web import Response, StreamResponse, View
from aiohttp.web_exceptions import HTTPBadRequest, HTTPFound
from aiohttp_jinja2 import render_template as render
from marshmallow import ValidationError as MarshmallowValidationError
from pydantic import ValidationError as PydanticValidationError

from server.core.base.dto import DTO
from server.core.base.facades import BaseFacade
from server.core.middleware.authenticate import logout
from server.settings import DEBUG


class BaseView(View):
    facade: Optional[BaseFacade] = None
    template: str

    async def _iter(self) -> StreamResponse:
        if DEBUG:
            return await super()._iter()
        else:
            try:
                return await super()._iter()
            except MarshmallowValidationError:
                # TODO: обработчик ошибок marshmallow
                raise logout(
                    self.request,
                    HTTPFound(
                        location=self.request.app.router['auth-signin'].url_for()
                    )
                )
            except PydanticValidationError:
                # TODO: обработчик ошибок pydantic
                raise logout(
                    self.request,
                    HTTPFound(
                        location=self.request.app.router['auth-signin'].url_for()
                    )
                )

    @property
    async def context(self):
        return (await self.facade.get_context(self.request)) if self.facade is not None else None

    def process_context(self, context):
        return context

    def _render(self, template: str, context: Optional[Union[DTO, Dict]] = None, **kwargs) -> Response:
        template_context = {}
        if context is not None:
            if isinstance(context, DTO):
                template_context = context.dict()
            else:
                template_context = context
        return render(
            template_name=template,
            request=self.request,
            context=template_context,
            **kwargs
        )

    async def render(self):

        context: DTO = self.process_context(await self.context)
        return self._render(self.template, context)
