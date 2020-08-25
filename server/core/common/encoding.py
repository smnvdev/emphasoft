import base64
from binascii import Error as BinasciiError
import datetime
from decimal import Decimal


_PROTECTED_TYPES = (
    type(None), int, float, Decimal, datetime.datetime, datetime.date, datetime.time,
)


def is_protected_type(obj):
    """Определяет, является ли объект экземпляром защищенного типа.

    """
    return isinstance(obj, _PROTECTED_TYPES)


def force_bytes(s, encoding='utf-8', strings_only=False, errors='strict'):
    """
    Возвращает байтовую строку 's', в кодировке укзанной в 'encoding'.
    Lazy instances преобразуются в строки.

    Если 'string_only' равно True, не конвертирует non-string-like объекты.
    """
    if isinstance(s, bytes):
        if encoding == 'utf-8':
            return s
        else:
            return s.decode('utf-8', errors).encode(encoding, errors)
    if strings_only and is_protected_type(s):
        return s
    if isinstance(s, memoryview):
        return bytes(s)
    return str(s).encode(encoding, errors)


def urlsafe_base64_decode(s):
    s = s.encode()
    try:
        return base64.urlsafe_b64decode(s.ljust(len(s) + len(s) % 4, b'='))
    except (LookupError, BinasciiError) as e:
        raise ValueError(e)


def force_text(s, encoding='utf-8', strings_only=False, errors='strict'):
    if issubclass(type(s), str):
        return s
    if strings_only and isinstance(s, (type(None), int, float, Decimal, datetime.datetime, datetime.date, datetime.time,)):
        return s
    if isinstance(s, bytes):
        s = str(s, encoding, errors)
    else:
        s = str(s)
    return s
