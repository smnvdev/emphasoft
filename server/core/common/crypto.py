"""
Криптографические функции.
"""
import hashlib
import hmac
import random
import time

from server import settings
from server.core.common.encoding import force_bytes


try:
    random = random.SystemRandom()
    using_sys_random = True
except NotImplementedError:
    import logging
    logging.warning('Безопасный генератор псевдослучайных чисел недосупен'
                    'в вашей системе. Будет использован Вихрь Мерсенна (Mersenne Twister).')
    using_sys_random = False


def get_random_string(length=12,
                      allowed_chars='abcdefghijklmnopqrstuvwxyz'
                                    'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'):
    """
    Возвращает надежно сгенерированную случайную строку.
    """
    if not using_sys_random:
        random.seed(
            hashlib.sha256(
                ('%s%s%s' % (random.getstate(), time.time(), settings.SECRET_KEY)).encode()
            ).digest()
        )
    return ''.join(random.choice(allowed_chars) for i in range(length))


def constant_time_compare(val1, val2):
    """Возвращает True если две строки эквивалентны, иначе False."""
    return hmac.compare_digest(force_bytes(val1), force_bytes(val2))


def get_random_secret_key():
    """
    Возвращает рандомную строку состоящую из 50 символов.
    """
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
    return get_random_string(50, chars)
