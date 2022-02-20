import time
from typing import (NoReturn, Union)

class url:
    @staticmethod
    def field(w) -> str:    return "air_daily"

    @staticmethod
    def location(s: str) -> str: return s

    @staticmethod
    def public_key(s: str) -> str:  return s

    @staticmethod
    def ts() -> str:    return time.time()

    @staticmethod
    def ttl() -> str:
        ...

    @staticmethod
    def sig() -> str:
        ...

