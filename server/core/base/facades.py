from asyncio import gather
from typing import Dict, List, Tuple, Type

from aiohttp import ClientSession

from server.core.base.dto import DTO
from server.core.gateways.base import APIGateway


class BaseFacade:
    """
        Базовый класс фасада. Фасад является классом управления, который
        собирает в себя шлюзы, а затем при вызове get_context осуществляет
        ассинхронные вызовы всех имплементированных в него шлюзов. После завершения всех тасков
        шлюзов - возвращяет определенный в нем контекст.
    """
    gateways: Dict[str, APIGateway]
    context: Type[DTO]

    @staticmethod
    def process_context(context):
        return context

    @staticmethod
    async def __execute_gateway(session, name, gateway):
        return name, await gateway.execute(session)

    @staticmethod
    def get_header(request):
        headers = {
            'Content-Type': 'application/json',
        }
        return headers

    async def get_context(self, request):
        headers = self.get_header(request)
        async with ClientSession(headers=headers) as session:
            tasks = [
                self.__execute_gateway(session, name, gateway)
                for name, gateway in self.gateways.items()
            ]
            data: List[Tuple[str, DTO]] = await gather(*tasks, return_exceptions=False)
            context = self.context(**dict(data))
            return self.process_context(context)

    def update(self, gateways: Dict[str, APIGateway]):
        self.gateways = self.gateways.copy()
        self.gateways.update(gateways)
