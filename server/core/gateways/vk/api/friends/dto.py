from typing import Optional

from server.core.base.dto import DTO


class VKCityDTO(DTO):
    id: int
    title: str


class VKFriendDTO(DTO):
    id: int
    first_name: str
    last_name: str
    is_closed: Optional[bool]
    can_access_closed: Optional[bool]
    online: int
    track_code: str

    nickname: Optional[str]
    domain: Optional[str]
    sex: Optional[int]
    bdate: Optional[str]
    city: Optional[VKCityDTO]

    photo_50: Optional[str]
    photo_100: Optional[str]
    photo_200_orig: Optional[str]
