from enum import Enum


class PyEnum(Enum):

    @classmethod
    def list(cls) -> list:
        return list(map(lambda x: x.value, cls))
