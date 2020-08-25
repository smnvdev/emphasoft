from typing import Generic, List, Optional, TypeVar
from pydantic.generics import GenericModel

from server.core.base.dto import DTO

ResultsT = TypeVar('ResultsT')


class ResponseContentDTO(GenericModel, Generic[ResultsT]):
    count: int
    items: List[ResultsT]


class ResponseDTO(DTO):
    response: ResponseContentDTO
