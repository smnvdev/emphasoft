from server.settings import VK_APP_ID


async def processor(request, *args, **params):
    return {
        'request': request,
        'vk_app_id': VK_APP_ID
    }
