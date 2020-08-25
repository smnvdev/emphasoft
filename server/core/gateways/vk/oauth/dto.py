from typing import Optional

from server.core.base.dto import DTO


class VkOAuthAccessTokenDTO(DTO):
    access_token: str
    expires_in: int
    user_id: int
    email: Optional[str]
