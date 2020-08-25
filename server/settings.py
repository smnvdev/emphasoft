import os
import pathlib


###############
# APPLICATION #
###############

SECRET_KEY = os.getenv('SECRET_KEY', '123qweASD')

DEBUG = os.getenv('DEBUG', 'False') == 'True'

AUTH_COOKIE_NAME = os.getenv('AUTH_COOKIE_NAME', 'authToken')

MIDDLEWARE = [
    'aiohttp.web_middlewares.normalize_path_middleware',
    'server.core.middleware.VKOAuthMiddleware',
]

TEMPLATE_FILTERS = [
    'server.apps.auth.filters.OAuthVKLinkGenerationFilter',
]

PROJECT_ROOT = pathlib.Path(__file__).parent.parent
TEMPLATES_ROOT = PROJECT_ROOT / 'templates'
STATIC_ROOT = PROJECT_ROOT / 'static'

##############
# STATIC URL #
##############

STATIC_URL = '/static'

##################
# VK APPLICATION #
##################
VK_APP_ID = os.getenv('VK_APP_ID', None)
VK_APP_SECRET_KEY = os.getenv('VK_APP_SECRET_KEY', None)

VK_OAUTH_HOST = os.getenv('VK_OAUTH_HOST', 'https://oauth.vk.com')
VK_API_HOST = os.getenv('VK_API_HOST', 'https://api.vk.com')

OAUTH_REDIRECT_URI = os.getenv('OAUTH_REDIRECT_URI', 'https://semenov.fvds.ru/auth/callback')

#########
# REDIS #
#########
REDIS_URL = os.getenv('REDIS_URL', 'redis://redis:6379')
REDIS_DB_INDEX = int(os.getenv('REDIS_DB_INDEX', 0))
