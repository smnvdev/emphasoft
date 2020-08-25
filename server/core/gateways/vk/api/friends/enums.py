from enum import Enum


class VKFriendsOrderEnum(Enum):
    HINTS = 'hints'
    RANDOM = 'random'
    MOBILE = 'mobile'
    NAME = 'name'


class VKSexEnum(Enum):
    NONE = 0
    FEMALE = 1
    MALE = 2


class VKFriendsAdditionalField(Enum):
    NICKNAME = 'nickname'
    DOMAIN = 'domain'
    SEX = 'sex',
    BIRTH_DATE = 'bdate'
    CITY = 'city'
    COUNTRY = 'country'
    TIMEZONE = 'timezone'
    PHOTO_50 = 'photo_50'
    PHOTO_100 = 'photo_100'
    PHOTO_200_ORIG = 'photo_200_orig'
    HAS_MOBILE = 'has_mobile'
    CONTACTS = 'contacts'
    EDUCATION = 'education'
    ONLINE = 'online'
    RELATION = 'relation'
    LAST_SEEN = 'last_seen'
    STATUS = 'status'
    CAN_WRITE_PRIVATE_MESSAGE = 'can_write_private_message'
    CAN_SEE_ALL_POSTS = 'can_see_all_posts'
    CAN_POST = 'can_post'
    UNIVERSITIES = 'universities'


class VKNameCase(Enum):
    NOM = 'nom'  # Именительны падеж
    GEN = 'gen'  # Родительный падеж
    DAT = 'dat'  # Дательный ...
    ACC = 'acc'  # Винительный ...
    INS = 'ins'  # Творительный ...
    ABL = 'abl'  # Предложный ...

