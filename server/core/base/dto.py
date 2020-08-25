from pydantic import BaseModel


class DTO(BaseModel):
    """Базовая Data Transfer Object модель."""

    class Config:
        extra = 'ignore'
