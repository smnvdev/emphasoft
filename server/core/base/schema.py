from marshmallow import Schema, EXCLUDE


class BaseSchema(Schema):
    """Базовый класс для схемы данных."""
    class Meta:
        abstract = True
        unknown = EXCLUDE
